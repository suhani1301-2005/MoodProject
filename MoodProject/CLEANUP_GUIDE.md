# Project Cleanup Guide - Safe Removal Steps

This guide helps you clean up unnecessary files and folders **without breaking the project**.

---

## ✅ SAFE TO DELETE (Tested & Verified)

### 1. **__pycache__ Folders** (Python Bytecode Cache)
These are automatically generated and will be recreated when needed.

**Folders to remove:**
- `config/__pycache__/`
- `recommender/__pycache__/`
- `recommender/migrations/__pycache__/`

**How to remove:**
```powershell
# PowerShell command
Get-ChildItem -Path "d:\AWD final Project\MoodProject" -Recurse -Directory -Name "__pycache__" | ForEach-Object { Remove-Item -Path "d:\AWD final Project\MoodProject\$_" -Recurse -Force }
```

**Or manually:**
- Right-click on each `__pycache__` folder → Delete

---

### 2. **.pyc Files** (Compiled Python Files)
Multiple Python versions have compiled these files (Python 3.10 and 3.13).

**Files found:**
- `config/__pycache__/*.pyc`
- `recommender/__pycache__/*.pyc`
- `recommender/migrations/__pycache__/*.pyc`

**How to remove:**
```powershell
Get-ChildItem -Path "d:\AWD final Project\MoodProject" -Recurse -Filter "*.pyc" -Force | Remove-Item -Force
```

---

### 3. **Unused Music Files** (4 songs not in any playlist)
These songs are **NOT** used in any playlist configuration in `views.py`.

**Unused songs to delete from `static/music/`:**
- `Badtameez Dil.mp3`
- `Kurchi Madathapetti.mp3`
- `Party All Night.mp3`
- `Shararat.mp3`

**Currently used songs (DO NOT DELETE):**
- Happy playlist: 7 songs (Saiyara, Gallan Goodiyan, etc.)
- Sad playlist: 7 songs (Channa Mereya, Tum Hi Ho, etc.)
- Stressed playlist: 7 songs (Baarish1, Aaya Re Toofan, etc.)

**How to remove:**
```powershell
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Badtameez Dil.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Kurchi Madathapetti.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Party All Night.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Shararat.mp3" -Force
```

---

### 4. **Unused Image Files** (1 image not referenced)
This image is **NOT** used anywhere in the project.

**Unused image to delete from `static/images/`:**
- `happy_image.jpg`

**Currently used images (DO NOT DELETE):**
- `background1.png` - Used as page background
- `sad.jpg` - Used in sad mood playlist
- `stressed.jpg` - Used in stressed mood playlist
- `p3.jpg` - Used in happy mood playlist

**How to remove:**
```powershell
Remove-Item -Path "d:\AWD final Project\MoodProject\static\images\happy_image.jpg" -Force
```

---

### 5. **db.sqlite3** (Optional - SQLite Database)
This database stores Django's default admin users and logs (if not using MongoDB for everything).

**Status:** Can be deleted and will be recreated on next `python manage.py migrate`

**How to remove:**
```powershell
Remove-Item -Path "d:\AWD final Project\MoodProject\db.sqlite3" -Force
```

---

## 🚫 DO NOT DELETE (Critical Files)

| File/Folder | Reason |
|---|---|
| `manage.py` | Django project management (CRITICAL) |
| `config/` folder | Django settings and configuration (CRITICAL) |
| `config/settings.py` | Database & app configuration (CRITICAL) |
| `config/urls.py` | URL routing (CRITICAL) |
| `config/wsgi.py` | Production server config (CRITICAL) |
| `recommender/` folder | Main app with all logic (CRITICAL) |
| `recommender/views.py` | Handles all requests (CRITICAL) |
| `recommender/utils.py` | Mood detection AI logic (CRITICAL) |
| `recommender/urls.py` | App routing (CRITICAL) |
| `recommender/models.py` | Database models (CRITICAL) |
| `recommender/mongo.py` | MongoDB connection (CRITICAL) |
| `requirements.txt` | Python dependencies (CRITICAL) |
| `templates/` folder | All HTML templates (CRITICAL) |
| `static/css/style.css` | All styling (CRITICAL) |
| `static/music/` | Keep all 21 used songs |
| `static/images/` | Keep 4 used images |

---

## 📋 Cleanup Checklist

### **Option 1: Full Cleanup** (Recommended)
Remove all safe items for maximum space savings:

```powershell
# Remove all __pycache__ folders
Get-ChildItem -Path "d:\AWD final Project\MoodProject" -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force

# Remove unused music files
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Badtameez Dil.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Kurchi Madathapetti.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Party All Night.mp3" -Force
Remove-Item -Path "d:\AWD final Project\MoodProject\static\music\Shararat.mp3" -Force

# Remove unused image
Remove-Item -Path "d:\AWD final Project\MoodProject\static\images\happy_image.jpg" -Force
```

### **Option 2: Safe Cleanup** (Recommended for Beginners)
Only remove auto-generated files (safest option):

```powershell
# Remove only __pycache__ folders
Get-ChildItem -Path "d:\AWD final Project\MoodProject" -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

---

## ✅ After Cleanup Verification

After deleting files, verify the project still works:

```bash
# 1. Navigate to project folder
cd "d:\AWD final Project\MoodProject"

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Run the server
python manage.py runserver

# 4. Test in browser
# Open http://127.0.0.1:8000/
```

**Expected behavior:**
- ✅ Login page loads
- ✅ Can register and login
- ✅ Can select mood
- ✅ Can listen to songs (21 working songs)
- ✅ Mood detection works
- ✅ History page displays stats

---

## 🔄 Automatic Cache Recreation

**Important:** Python will automatically recreate:
- `__pycache__` folders
- `.pyc` files

This happens when you run:
- `python manage.py runserver`
- `python manage.py migrate`
- Or any Python execution

**This is normal and safe!**

---

## 📊 Space Savings Summary

| Item | Size | Space Saved |
|---|---|---|
| __pycache__ folders | ~5-10 MB | Recretaed automatically |
| .pyc files | ~3-5 MB | Automatically recreated |
| Unused songs (4 files) | ~35-40 MB | Permanent |
| Unused image (1 file) | ~200-300 KB | Permanent |
| **Total Cleanup Potential** | **~40-50 MB** | ✅ Safe to delete all |

---

## 🆘 If Something Breaks

**If the project stops working after cleanup:**

1. **Don't worry!** Your code is still intact
2. The most likely issue: You deleted a critical file
3. **Solution:** Restore from backup or reinstall dependencies:

```powershell
# Reinstall dependencies
pip install -r requirements.txt

# Recreate database
python manage.py migrate

# Run server again
python manage.py runserver
```

---

**Last Updated:** April 23, 2026  
**Project:** Mood-Based Music Recommendation System
