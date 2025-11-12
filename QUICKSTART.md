# 🚀 Quick Start Guide

## Option 1: Automated Setup (Recommended)

Run the setup script:

```powershell
.\setup.ps1
```

This will automatically:
- Create a virtual environment
- Install all dependencies
- Set up the database
- Load all challenges
- Prompt you to create an admin account

Then start the server:

```powershell
python manage.py runserver
```

## Option 2: Manual Setup

### Step 1: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 3: Set Up Database

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Load Challenges

```powershell
python manage.py init_challenges
```

### Step 5: Create Admin Account

```powershell
python manage.py createsuperuser
```

### Step 6: Run the Server

```powershell
python manage.py runserver
```

## Access the Application

- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Default URLs

- `/` - Home page
- `/register/` - Player registration
- `/login/` - Player login
- `/dashboard/` - Game dashboard
- `/leaderboard/` - Global leaderboard
- `/profile/` - Player profile
- `/admin/` - Admin panel

## Testing the Game

1. Register a new player account
2. Start with Part 1: The Chrono Bridge
3. Submit answer: `flag{13}`
4. Progress through all 7 challenges

## Admin Panel Features

Login to `/admin/` to:
- View all players and scores
- Manage challenges
- Monitor submissions
- Track hint usage

## Troubleshooting

### Port Already in Use?

```powershell
python manage.py runserver 8080
```

### Need to Reset Database?

```powershell
Remove-Item db.sqlite3
python manage.py migrate
python manage.py init_challenges
python manage.py createsuperuser
```

### Virtual Environment Issues?

```powershell
deactivate
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

**Ready to begin your mission, Agent?** 🌌
