# 🎵 Mood-Based Music Recommendation System

A **Django web application** that intelligently recommends music based on your mood using AI sentiment analysis. The system detects your emotional state from text input or manual selection and creates personalized music playlists.

---

## 📋 Table of Contents

1. [Features](#-features)
2. [Technologies Used](#-technologies-used)
3. [Project Structure](#-project-structure)
4. [How to Run](#-how-to-run)
5. [Important Files Explained](#-important-files-explained)
6. [How It Works](#-how-it-works)
7. [Future Improvements](#-future-improvements)

---

## ✨ Features

### 🎯 **Core Features**
- **User Authentication** - Secure login and signup system using bcrypt password hashing
- **Manual Mood Selection** - Choose from 3 mood categories: Happy, Sad, Stressed
- **AI Mood Detection** - Advanced sentiment analysis to detect mood from text input
- **Dynamic UI** - Background colors and themes change based on detected mood
- **Music Player** - Play, pause, and stop songs with a modern interface
- **Mood History** - View your mood history with date/time tracking
- **Mood Analytics** - Visual graph showing mood statistics

### 🎧 **Music Features**
- **21 Bollywood Songs** - Curated playlist for each mood category
- **Single Player** - Only one song plays at a time (no overlapping audio)
- **Stop Button** - Manually stop playback on the same page
- **Play/Pause Control** - Toggle music playback easily
- **Now Playing Display** - See current song title and artist

### 📊 **Analytics Features**
- Track mood patterns over time
- View percentage distribution of moods
- Date-based mood history with timestamps
- Beautiful statistics visualization

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Backend programming language |
| **Django 6.0.4** | Web framework for building the application |
| **MongoDB** | NoSQL database for storing user and mood history |
| **TextBlob** | AI library for sentiment analysis (mood detection) |
| **SQLite** | Default Django database (optional) |
| **HTML5** | Frontend structure |
| **CSS3** | Styling and animations |
| **JavaScript (Vanilla)** | Interactive features and audio control |
| **bcrypt** | Password encryption for security |

---

## 📁 Project Structure

```
MoodProject/
├── manage.py                    # Django command-line utility (run server, migrations)
├── db.sqlite3                   # SQLite database (optional)
├── requirements.txt             # List of all Python dependencies
│
├── config/                      # Django main configuration folder
│   ├── __init__.py             # Makes folder a Python package
│   ├── settings.py             # Django configuration (database, apps, security)
│   ├── urls.py                 # Main URL routing (maps URLs to views)
│   ├── asgi.py                 # Async server config (for production)
│   └── wsgi.py                 # WSGI server config (for production deployment)
│
├── recommender/                 # Main application folder with all logic
│   ├── __init__.py
│   ├── admin.py                # Django admin panel configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models (defines how data is stored)
│   ├── views.py                # Request handlers (processes user actions)
│   ├── urls.py                 # App-specific URL routing
│   ├── forms.py                # Form classes for user input
│   ├── utils.py                # Helper functions (mood detection logic)
│   ├── mongo.py                # MongoDB connection and collections setup
│   ├── tests.py                # Unit tests
│   │
│   └── migrations/             # Database migration history
│       ├── __init__.py
│       └── 0001_initial.py     # Initial database structure
│
├── templates/                   # HTML template files
│   ├── base.html               # Base template (header, navbar, footer)
│   ├── index.html              # Home page with mood selection
│   ├── login.html              # User login page
│   ├── signup.html             # User registration page
│   ├── mood_input.html         # AI mood detection form (text input)
│   ├── mood_result.html        # Shows detected mood and recommendation
│   ├── playlist.html           # Main music player with 21 songs
│   ├── history.html            # User's mood history and statistics
│   ├── result.html             # Search/discovery results
│   └── analytics.html          # Analytics and mood graph
│
└── static/                      # Static files (CSS, images, music)
    ├── css/
    │   └── style.css           # All styling and animations
    ├── images/                 # Album covers and UI images
    │   ├── background1.png     # Page background
    │   ├── happy_image.jpg     # Happy mood icon
    │   ├── sad.jpg             # Sad mood icon
    │   ├── stressed.jpg        # Stressed mood icon
    │   └── p3.jpg              # Happy playlist cover
    │
    └── music/                  # 21 Bollywood songs
        ├── Happy Playlist (7 songs)
        │   ├── Saiyara.mp3
        │   ├── Gallan Goodiyan.mp3
        │   ├── Abhi Toh Party Shuru Hui Hai.mp3
        │   ├── Ghagra.mp3
        │   ├── Chunnari.mp3
        │   ├── Kar Gayi Chull.mp3
        │   └── Matargashti.mp3
        │
        ├── Sad Playlist (7 songs)
        │   ├── Channa Mereya.mp3
        │   ├── Tum Hi Ho.mp3
        │   ├── Agar Tum Saath Ho.mp3
        │   ├── Baarish.mp3
        │   ├── Kabira.mp3
        │   ├── Ranjha.mp3
        │   └── Tum Se Hi.mp3
        │
        └── Stressed Playlist (7 songs)
            ├── Baarish1.mp3
            ├── Aaya Re Toofan.mp3
            ├── Dilbaro.mp3
            ├── Luka Chuppi.mp3
            ├── Teri Mitti.mp3
            ├── Shaky.mp3
            └── Challa.mp3
```

---

## 🚀 How to Run

### **Prerequisites**
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (venv)

### **Step 1: Clone/Extract Project**
```bash
cd "d:\AWD final Project\MoodProject"
```

### **Step 2: Create Virtual Environment**
```bash
# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Run Database Migrations**
```bash
python manage.py migrate
```

### **Step 5: Start the Server**
```bash
python manage.py runserver
```

### **Step 6: Open in Browser**
```
http://127.0.0.1:8000/
```

---

## 📚 Important Files Explained

### **1. `recommender/views.py` - The Brain of the Application**

**What it does:**
- Handles all user requests and responses
- Processes user actions (login, signup, mood selection)
- Retrieves data from database
- Sends data to templates for display

**Key Functions:**

| Function | Purpose |
|---|---|
| `register()` | Handles user signup with password encryption |
| `user_login()` | Authenticates user credentials |
| `user_logout()` | Clears user session |
| `home()` | Displays home page with mood selection |
| `playlist_view()` | Shows playlist with 21 songs for selected mood |
| `mood_input_view()` | Shows form for AI mood detection |
| `mood_detect_view()` | Processes text input and detects mood using AI |
| `history()` | Displays user's mood history and statistics |

**In Simple Terms:**
Think of `views.py` as a **waiter in a restaurant**:
- User makes a request (clicks a button)
- Waiter (view) processes the request
- Waiter brings back data from kitchen (database)
- Waiter serves the response (HTML page)

---

### **2. `recommender/utils.py` - The AI Brain**

**What it does:**
- Detects mood from user text input using sentiment analysis
- Uses TextBlob library to analyze emotions

**Key Function: `detect_mood(text)`**

**How it works:**
```python
Input: "I am so happy and excited!"
     ↓
TextBlob analyzes text sentiment (polarity score: -1 to 1)
     ↓
     • polarity > 0.3 → "Happy" 😊
     • polarity < -0.3 → "Sad" 😢
     • otherwise → "Stressed" 😤
     ↓
Output: "Happy"
```

**Examples:**
- `detect_mood("I feel wonderful!")` → "Happy"
- `detect_mood("I'm so sad and lonely")` → "Sad"
- `detect_mood("I don't know what to feel")` → "Stressed"

---

### **3. `recommender/models.py` - Data Structure**

**What it does:**
- Defines how data is stored in the database
- Creates the `MoodHistory` table in SQLite

**MoodHistory Model:**
```python
MoodHistory
├── user (Foreign Key) - links to user account
├── mood (CharField) - "Happy", "Sad", or "Stressed"
├── created_at (DateTime) - when mood was recorded
```

**In Simple Terms:**
This is like creating a **form** with these fields:
- Which user recorded this mood?
- What mood did they select/detect?
- When did they record it?

---

### **4. `recommender/mongo.py` - MongoDB Connection**

**What it does:**
- Connects to MongoDB database
- Creates collections for users and mood history
- Stores user login credentials and mood records

**Collections:**

| Collection | Stores |
|---|---|
| `users_collection` | Username and bcrypt hashed passwords |
| `mood_history_collection` | User mood records with timestamps |

**In Simple Terms:**
This is the **library** that manages the filing system where data is stored.

---

### **5. `templates/playlist.html` - Music Player Interface**

**What it does:**
- Displays the music player
- Lists all 21 songs
- Handles play/pause/stop functionality

**Key JavaScript Functions:**

| Function | Action |
|---|---|
| `playSong(file, element)` | Plays selected song |
| `togglePlay()` | Play/pause toggle |
| `stopSong()` | Stops music and resets player |
| `filterTracks(mood)` | Filter songs by mood |

**UI Components:**
- 📋 Track list (showing all songs)
- ⏮⏭ Previous/Next buttons
- ▶⏸ Play/Pause button
- ⏹ **Stop button** (NEW - stops music immediately)
- 📊 Progress bar showing song duration
- 🔊 Now playing display

---

### **6. `static/css/style.css` - All Styling**

**What it does:**
- Styles all HTML elements
- Creates mood-based themes (Happy=Golden, Sad=Blue, Stressed=Pink)
- Animations and hover effects
- Responsive design

**Color Schemes:**
- 😊 **Happy:** Golden/Yellow (#FFD89B)
- 😢 **Sad:** Dark Blue/Purple (#667eea)
- 😤 **Stressed:** Pink/Red (#f093fb)

---

### **7. `recommender/mongo.py` - Database Setup**

**What it does:**
```python
from pymongo import MongoClient

# Connects to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mood_database']

# Creates or accesses collections
users_collection = db['users']
mood_history_collection = db['mood_history']
```

**In Simple Terms:**
This establishes the **connection** to the filing system (MongoDB) so we can read/write user data.

---

## 🧠 How It Works (Complete Flow)

### **User Journey:**

```
1. USER ARRIVES AT WEBSITE
   ↓
   Browser: http://127.0.0.1:8000/
   Django: Route → urls.py → home view
   Page: Login page displayed
   ↓

2. USER SIGNS UP / LOGS IN
   ↓
   Form submitted → views.py (register/user_login)
   Password encrypted with bcrypt
   Data stored in MongoDB
   Session created
   ↓

3. USER SELECTS MOOD (Two Options)
   ↓
   Option A: Manual Selection
   └─ Click "Happy/Sad/Stressed"
      → Views.py receives mood
      → Data saved to MongoDB
      → Redirect to playlist
   ↓
   Option B: AI Detection
   └─ Enter text → "I'm feeling great!"
      → views.py calls utils.py
      → TextBlob analyzes sentiment
      → detect_mood() returns mood
      → Mood displayed to user
      → User clicks "Play Playlist"
      → Redirect to playlist
   ↓

4. USER SEES MUSIC PLAYER
   ↓
   Playlist.html displayed
   - 7 songs for selected mood shown
   - Audio player ready
   ↓

5. USER PLAYS MUSIC
   ↓
   Click song → playSong() JavaScript function
   ↓
   - Audio file loads: /static/music/songname.mp3
   - Player starts playing
   - Song title updated: "Now Playing: Saiyara"
   - Play icon changes to pause icon
   ↓

6. USER CAN:
   ↓
   ▶ Play/Pause → togglePlay() function
   ⏹ STOP → stopSong() function (NEW)
   📊 View progress bar
   ↓

7. USER CHECKS HISTORY
   ↓
   Click "History" → views.py (history function)
   ↓
   - Retrieves user's mood records from MongoDB
   - Calculates statistics
   - Displays graph
   - Shows date/time of each mood
   ↓

8. USER LOGS OUT
   ↓
   Click "Logout" → Session cleared → Redirect to login
```

---

## 🔐 Security Features

| Feature | How It Works |
|---|---|
| **Password Hashing** | bcrypt encryption (not plain text) |
| **Session Management** | Django session middleware |
| **Login Required** | Decorators check user authentication |
| **CSRF Protection** | Django CSRF tokens in forms |
| **Database Security** | MongoDB stores only hashed data |

---

## 📊 Database Schema

### **MongoDB Collections:**

**users_collection:**
```javascript
{
  _id: ObjectId,
  username: "john_doe",
  password: "$2b$12$..." // bcrypt hash
}
```

**mood_history_collection:**
```javascript
{
  _id: ObjectId,
  username: "john_doe",
  mood: "Happy",
  date: ISODate("2026-04-23T...")
}
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|---|---|
| **"ModuleNotFoundError"** | Run `pip install -r requirements.txt` |
| **"No module named 'pymongo'"** | `pip install pymongo` |
| **"Connection refused" (MongoDB)** | Install & start MongoDB service |
| **Songs not playing** | Check if files exist in `/static/music/` |
| **Styles not loading** | Run `python manage.py collectstatic` |
| **Login not working** | Check MongoDB is running |

---

## 🚀 Future Improvements

### **Feature Enhancements:**
- ✨ **Spotify Integration** - Connect real Spotify playlists
- 🎤 **Voice Recognition** - Detect mood from voice input
- 👥 **Social Features** - Share playlists with friends
- ❤️ **Favorites** - Save favorite songs
- 📱 **Mobile App** - Native iOS/Android app
- 🌍 **Multi-Language** - Support multiple languages
- 🎵 **More Songs** - Expand music library to 1000+ songs

### **Technical Improvements:**
- 🔄 **Caching** - Redis for faster loading
- 📈 **Scalability** - PostgreSQL instead of SQLite
- 🔍 **Search** - Full-text search for songs
- 🎨 **Advanced Analytics** - Mood trend predictions
- 🔒 **Email Verification** - OTP-based signup
- 🤖 **ML Models** - Better emotion detection

### **UI/UX Improvements:**
- 🎨 **Dark Mode** - Eye-friendly dark theme
- 📱 **Responsive Design** - Better mobile experience
- 🎬 **Animations** - Smooth transitions
- 👤 **User Profile** - Personal user dashboard
- 🎯 **Recommendations** - Smart song suggestions

---

## 📝 Project Information

| Detail | Value |
|---|---|
| **Project Name** | Mood-Based Music Recommendation System |
| **Framework** | Django 6.0.4 |
| **Database** | MongoDB + SQLite |
| **Python Version** | 3.10+ |
| **Status** | ✅ Production Ready |
| **License** | Open Source |

---

## 👨‍💻 What Problem Does This Solve?

### **The Problem:**
People have different moods throughout the day (Happy, Sad, Stressed) but struggle to find suitable music quickly.

### **The Solution:**
This application **automatically detects your mood** using AI and creates a **personalized playlist** instantly.

### **Benefits:**
- ✅ Save time finding music
- ✅ Improve emotional well-being
- ✅ Track mood patterns
- ✅ Discover songs based on emotion
- ✅ Beautiful, intuitive interface

---

## 📞 Support & Questions

For issues or questions about specific features:

1. Check the **Troubleshooting** section above
2. Review code comments in relevant files
3. Check Django/MongoDB documentation
4. Test with sample data first

---

## 📜 License

This project is open source and available for educational purposes.

---

**Last Updated:** April 23, 2026  
**Created For:** Educational/Learning Purpose  
**Status:** ✅ Fully Functional

---

## 🎓 For Viva/Exam Explanation

### **Quick 30-Second Explanation:**
> "This is a Django web application that recommends Bollywood songs based on your mood. Users can either select a mood manually (Happy, Sad, Stressed) or enter text, and the AI uses TextBlob sentiment analysis to detect their emotional state. The system then plays a personalized playlist of 7 songs from MongoDB. It also tracks mood history with analytics."

### **Key Points to Mention:**
1. **Technology Stack:** Django, MongoDB, TextBlob, HTML/CSS/JS
2. **Main Feature:** AI mood detection using sentiment analysis
3. **Database:** MongoDB for scalability, SQLite for Django
4. **Security:** bcrypt password hashing, session management
5. **Music Player:** Stop/Play/Pause functionality with 21 songs
6. **Analytics:** Mood history tracking with statistics

### **Difficult Questions & Answers:**

**Q: Why did you use MongoDB instead of just SQLite?**
> MongoDB is better for storing flexible data (user moods can have extra fields in future). It's also more scalable.

**Q: How does mood detection work?**
> TextBlob calculates sentiment polarity (-1 to 1). Positive scores mean Happy, negative mean Sad, neutral mean Stressed.

**Q: Why use bcrypt for passwords?**
> bcrypt is one-way encryption. Even if database is hacked, attackers can't reverse passwords. Much safer than plain text.

---

**Congratulations! Your project is fully documented!** 🎉
