from .mongo import users_collection, mood_history_collection
import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MoodHistory
from .utils import detect_mood  # ✅ Import mood detection function
from datetime import datetime


# ===== REGISTER =====
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")

        if users_collection.find_one({"username": username}):
            messages.error(request, "User already exists")
            return redirect("register")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        users_collection.insert_one({
            "username": username,
            "password": hashed_password
        })

        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "signup.html")


# ===== LOGIN =====
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = users_collection.find_one({"username": username})

        if user:
            stored_password = user['password']

            # 🔐 Case 1: bcrypt hashed (bytes)
            if isinstance(stored_password, (bytes, bytearray)):
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    request.session['user'] = username
                    return redirect("home")
                else:
                    messages.error(request, "Wrong password")

            # ⚠️ Case 2: old plain text users (temporary support)
            else:
                if password == stored_password:
                    request.session['user'] = username
                    return redirect("home")
                else:
                    messages.error(request, "Wrong password")

        else:
            messages.error(request, "User not found")

    return render(request, "login.html")

# ===== LOGOUT =====
def user_logout(request):
    request.session.flush()   # ✅ FIXED
    return redirect('login')


# ===== HOME =====
def home(request):
    if not request.session.get('user'):   # ✅ custom auth check
        return redirect('login')

    if request.method == "POST":
        mood = request.POST.get("mood")
        username = request.session['user']
        
        # Save mood to MongoDB
        mood_history_collection.insert_one({
            "username": username,
            "mood": mood,
            "date": datetime.now()
        })

        return redirect('playlist', mood.lower())

    return render(request, "index.html")


# ===== HISTORY =====
def history(request):
    if not request.session.get('user'):
        return redirect('login')
    
    username = request.session['user']
    
    # Get user's mood history from MongoDB
    data = list(mood_history_collection.find({"username": username}).sort("date", -1))
    
    # Calculate stats
    total = len(data)
    happy = sum(1 for item in data if item['mood'] == 'Happy')
    sad = sum(1 for item in data if item['mood'] == 'Sad')
    stressed = sum(1 for item in data if item['mood'] == 'Stressed')
    
    # Format dates for display
    for item in data:
        item['date_formatted'] = item['date'].strftime('%Y-%m-%d %I:%M %p')

    return render(request, "history.html", {
        "data": data,
        "total": total,
        "happy": happy,
        "sad": sad,
        "stressed": stressed,
    })

# ===== PLAYLIST VIEW =====
def playlist_view(request, name):

    playlists = {
        "happy": {
            "title": "Bollywood Feel Good Songs",
            "image": "images/p3.jpg",
            "songs": [
                {"title": "Saiyara", "artist": "Mohit Chauhan", "file": "saiyara.mp3"},
                {"title": "Abhi Toh Party Shuru Hui Hai", "artist": "Honey Singh", "file": "Abhi Toh Party Shuru Hui Hai.mp3"},
                {"title": "Ghagra", "artist": "Sunidhi Chauhan", "file": "Ghagra.mp3"},
                {"title": "Chunnari Chunnari", "artist": "Shreya Ghoshal", "file": "Chunnari.mp3"},
                {"title": "Kar Gayi Chull", "artist": "Arijit Singh", "file": "Kar Gayi Chull.mp3"},
                {"title": "Matargashti", "artist": "Bappi Lahiri", "file": "Matargashti.mp3"},
                 {"title": "Gallan Goodiyan", "artist": "Farhan Akhtar", "file": "GallanGoodiyan.mp3"},
            ]
        },

        "sad": {
            "title": "Sad Mood Songs 💔",
            "image": "images/sad.jpg",
            "songs": [
                {"title": "Channa Mereya", "artist": "Arijit Singh", "file": "Channa Mereya.mp3"},
                {"title": "Tum Hi Ho", "artist": "Arijit Singh", "file": "Tum Hi Ho.mp3"},
                {"title": "Agar Tum Saath Ho", "artist": "Alka Yagnik", "file": "Agar Tum Saath Ho.mp3"},
                {"title": "Baarish", "artist": "Arijit Singh", "file": "Baarish.mp3"},
                {"title": "Kabira", "artist": "Arijit Singh", "file": "Kabira.mp3"},
                {"title": "Ranjha", "artist": "Benny Dayal", "file": "Ranjha.mp3"},
                {"title": "Tum Se Hi", "artist": "Mohit Chauhan", "file": "TumSeHi.mp3"},

            ]
        },

        "stressed": {
            "title": "Relax & Chill 🌿",
            "image": "images/stressed.jpg",
            "songs": [
                {"title": "Baarish1", "artist": "Arijit Singh", "file": "Baarish1.mp3"},
                {"title": "Aaya Re Toofan", "artist": "Shreya Ghoshal", "file": "AayaReToofan.mp3"},
                {"title": "Dilbaro", "artist": "Harshdeep Kaur", "file": "Dilbaro.mp3"},
                {"title": "Luka Chuppi", "artist": "Lata Mangeshkar", "file": "LukaChuppi.mp3"},
                {"title" : "Teri Mitti Kesari", "artist": "B Praak", "file": "TeriMitti.mp3"},
                {"title": "Shaky", "artist": "Shreya Ghoshal", "file": "Shaky.mp3"},
                {"title": "Challa", "artist": "Ammy Virk", "file": "Challa.mp3"},
            ]
        }
    }

    data = playlists.get(name, {})

    return render(request, "playlist.html", {
        "title": data.get("title"),
        "image": data.get("image"),
        "songs": data.get("songs", [])
    })


# ===== AI MOOD INPUT VIEW =====
def mood_input_view(request):
    """
    Display form for AI-based mood detection via text input.
    GET: Show the mood input form
    """
    if not request.session.get('user'):   # ✅ Check if user is logged in
        return redirect('login')
    
    return render(request, "mood_input.html")


# ===== AI MOOD DETECTION VIEW =====
def mood_detect_view(request):
    """
    Process mood detection from user input text using AI.
    POST: Accept textarea input, detect mood, save to history, show result
    """
    if not request.session.get('user'):   # ✅ Check if user is logged in
        return redirect('login')
    
    if request.method == "POST":
        # ✅ Get user input text
        mood_text = request.POST.get("mood_text", "").strip()
        username = request.session['user']
        
        # ✅ Validate input
        if not mood_text:
            messages.error(request, "Please enter some text to analyze!")
            return redirect('mood_input')
        
        # ✅ Detect mood using AI
        detected_mood = detect_mood(mood_text)
        
        # ✅ Save mood to MongoDB history
        mood_history_collection.insert_one({
            "username": username,
            "mood": detected_mood,
            "input_text": mood_text,  # Store original text for reference
            "date": datetime.now()
        })
        
        # ✅ Pass detected mood and input text to result template
        return render(request, "mood_result.html", {
            "detected_mood": detected_mood,
            "user_text": mood_text
        })
    
    # ✅ Redirect to mood input form if not POST
    return redirect('mood_input')


# ===== MOOD ANALYTICS VIEW =====
def analytics(request):
    """
    Display mood analytics dashboard with charts.
    Shows count of each mood for the logged-in user.
    """
    # ✅ Check if user is logged in
    if not request.session.get('user'):
        return redirect('login')
    
    username = request.session['user']
    
    # ✅ Fetch all mood entries for this user from MongoDB
    user_moods = list(mood_history_collection.find({"username": username}))
    
    # ✅ Count each mood type
    mood_counts = {
        "Happy": 0,
        "Sad": 0,
        "Stressed": 0
    }
    
    # Count moods
    for entry in user_moods:
        mood = entry.get("mood", "")
        if mood in mood_counts:
            mood_counts[mood] += 1
    
    # ✅ Calculate total moods
    total_moods = sum(mood_counts.values())
    
    # ✅ Calculate percentages for insights
    mood_percentages = {}
    if total_moods > 0:
        for mood, count in mood_counts.items():
            percentage = (count / total_moods) * 100
            mood_percentages[mood] = round(percentage, 1)
    else:
        mood_percentages = {"Happy": 0, "Sad": 0, "Stressed": 0}
    
    # ✅ Find most common mood
    most_common_mood = max(mood_counts, key=mood_counts.get) if total_moods > 0 else "None"
    
    # ✅ Pass data to template
    return render(request, "analytics.html", {
        "mood_counts": mood_counts,
        "mood_percentages": mood_percentages,
        "total_moods": total_moods,
        "most_common_mood": most_common_mood
    })