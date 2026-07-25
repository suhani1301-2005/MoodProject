# Step-by-Step Guide: Deploying MoodProject to Render & MongoDB Atlas

This guide walks you through deploying your Django + MongoDB project for free using **Render** and **MongoDB Atlas**.

---

## Phase 1: Setup Free MongoDB Atlas (Cloud MongoDB Database)

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) and create a free account.
2. Click **Create a Deployment** and choose the **M0 Free Tier**.
3. Under **Database Access**, create a database user:
   - **Username**: (e.g. `mooduser`)
   - **Password**: (Generate a strong password and save it)
4. Under **Network Access**, click **Add IP Address** -> Select **Allow Access from Anywhere (`0.0.0.0/0`)**.
5. Click **Connect** -> Choose **Drivers (Python)**.
6. Copy the connection string:
   ```
   mongodb+srv://mooduser:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
   *(Replace `<password>` with your actual database password).*

---

## Phase 2: Push Project to GitHub

1. Create a new repository on [GitHub](https://github.com/new) named `MoodProject`.
2. Push your project to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Prepare MoodProject for production deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/MoodProject.git
   git push -u origin main
   ```

---

## Phase 3: Deploy Web Service on Render

1. Sign up / Log in to [Render](https://render.com/).
2. Click **New +** -> **Web Service**.
3. Select **Build and deploy from a Git repository** and connect your GitHub repository `MoodProject`.
4. Configure the Web Service settings:
   - **Name**: `mood-recommender` (or your choice)
   - **Environment**: `Python 3`
   - **Region**: Nearest to you
   - **Branch**: `main`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn config.wsgi:application`
5. Scroll to **Environment Variables** and add:
   - `MONGO_URI`: `mongodb+srv://mooduser:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`
   - `SECRET_KEY`: `generate-a-random-secret-key-here`
   - `DEBUG`: `False`
   - `PYTHON_VERSION`: `3.11.0`
6. Click **Create Web Service**.

---

## Phase 4: Verification

1. Render will automatically run `./build.sh` and start `gunicorn`.
2. Once the deployment status turns **Live**, click on your Render site URL (e.g., `https://mood-recommender.onrender.com`).
3. Try registering a user and submitting a mood to verify connection with MongoDB Atlas!
