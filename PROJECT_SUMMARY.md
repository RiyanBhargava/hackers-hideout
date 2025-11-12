# 🌌 Chrono Nexus Protocol - Django CTF Game

## ✅ Project Complete!

Your Django CTF game server has been successfully created with all the features you requested!

## 📦 What's Included

### Core Features
✅ **7 Progressive Challenges** - From prime numbers to complex ciphers
✅ **Point System** - Variable scoring based on difficulty (100-500 points)
✅ **Hint System** - Strategic hints with point penalties (10-50 points)
✅ **Leaderboard** - Real-time player rankings
✅ **Progress Tracking** - Complete submission history
✅ **Sequential Unlocking** - Challenges unlock as you progress
✅ **Space Theme UI** - Immersive dark cyberpunk design

### Technical Implementation
✅ **Django 4.2** - Modern Python web framework
✅ **SQLite Database** - Easy setup, production-ready
✅ **User Authentication** - Secure login/registration
✅ **Admin Panel** - Full challenge and player management
✅ **Responsive Design** - Works on all devices
✅ **Answer Validation** - Smart flag format checking

## 🎮 Game Challenges

| Part | Challenge | Type | Points |
|------|-----------|------|--------|
| 1 | The Chrono Bridge | Prime Numbers | 100 |
| 2 | The Lunar Core | Geometric Sequence | 150 |
| 3 | The Signal Fragment | Binary to ASCII | 200 |
| 4 | The Paradox Core | Pattern Recognition | 250 |
| 5 | The Void Transmission | Hex to ASCII | 300 |
| 6 | The Martian Vault | Caesar Cipher | 350 |
| 7 | The Chrono Nexus Core | Final Combination | 500 |

**Total Possible Points**: 1,850 points (without hint penalties)

## 🚀 Quick Start

### Easiest Way (Run Setup Script):

```powershell
.\setup.ps1
python manage.py runserver
```

### Manual Setup:

```powershell
# 1. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up database
python manage.py makemigrations
python manage.py migrate

# 4. Load challenges
python manage.py init_challenges

# 5. Create admin
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

Open: **http://127.0.0.1:8000/**

## 📁 File Structure

```
hackers-hideout/
├── chrono_nexus/              # Django project
│   ├── settings.py            # Configuration
│   ├── urls.py                # Main routing
│   └── wsgi.py                # WSGI config
│
├── game/                      # Game app
│   ├── models.py              # Database models
│   ├── views.py               # Game logic
│   ├── urls.py                # App routing
│   ├── admin.py               # Admin config
│   └── management/
│       └── commands/
│           └── init_challenges.py
│
├── templates/                 # HTML templates
│   ├── base.html
│   └── game/
│       ├── home.html
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── challenge.html
│       ├── leaderboard.html
│       └── profile.html
│
├── static/
│   └── css/
│       └── style.css          # Space-themed CSS
│
├── manage.py                  # Django CLI
├── requirements.txt           # Dependencies
├── README.md                  # Full documentation
├── QUICKSTART.md              # Quick start guide
└── setup.ps1                  # Automated setup
```

## 🎯 How Players Use It

1. **Register** with username, email, and team name
2. **Login** to access the dashboard
3. **View challenges** - see all 7 parts with difficulty and points
4. **Solve sequentially** - complete Part 1 to unlock Part 2, etc.
5. **Use hints** - get help but lose points
6. **Submit flags** - all answers in `flag{answer}` format
7. **Track progress** - see submissions, score, and rank
8. **Compete** - climb the global leaderboard

## 🔐 Admin Features

Access at `/admin/` to:

- ✅ **Manage Challenges** - Add, edit, delete challenges
- ✅ **Monitor Players** - View all players and scores
- ✅ **Track Submissions** - See all answers submitted
- ✅ **Review Hints** - Monitor hint usage
- ✅ **Export Data** - Download player statistics

## 🎨 UI Highlights

- **Dark Space Theme** - Cyberpunk aesthetics with neon accents
- **Animated Elements** - Hover effects and transitions
- **Responsive Design** - Mobile-friendly layout
- **Color-Coded Difficulty** - Easy (green), Medium (orange), Hard (red)
- **Progress Indicators** - Visual feedback on completion
- **Real-time Messages** - Success/error notifications

## 🔧 Customization

### Add New Challenges

1. Go to admin panel
2. Click "Challenges" → "Add Challenge"
3. Fill in all fields
4. Save

### Change Point Values

Edit in admin or modify `init_challenges.py`

### Modify UI Theme

Edit `static/css/style.css` - all colors are in CSS variables

### Add Features

Common additions:
- Timer per challenge
- Team support
- Difficulty modes
- Achievements/badges
- Email notifications

## 📊 Scoring System

**Base Points**: 100-500 per challenge
**Hint Penalty**: 10-50 points deducted
**One-Time Bonus**: Points awarded only on first correct answer
**Progressive Difficulty**: Points increase with each part

## 🎓 Perfect For

- ACM/IEEE competitions
- Cybersecurity workshops
- Coding bootcamps
- CTF practice events
- Computer science clubs
- Hackathons

## 📝 Answers (Admin Reference)

1. `flag{13}` - Prime number
2. `flag{243}` - Geometric sequence
3. `flag{LunaRim}` - Binary decode
4. `flag{52}` - Pattern recognition
5. `flag{heart_of_the_nexus}` - Hex decode
6. `flag{temporal_loop}` - Caesar cipher
7. `flag{heart_of_the_nexus_LunaRim_13_52_243_temporal_loop}` - Final

## 🐛 Common Issues

**Django not found?**
```powershell
pip install django
```

**Migrations error?**
```powershell
python manage.py migrate --run-syncdb
```

**Static files not loading?**
```powershell
python manage.py collectstatic
```

**Port 8000 in use?**
```powershell
python manage.py runserver 8080
```

## 🌟 Next Steps

1. Run the setup script or follow manual setup
2. Create your admin account
3. Test the game by registering as a player
4. Customize challenges if needed
5. Deploy to production (optional)

## 🚀 Production Deployment

For production use:

1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Set up static file serving
6. Use a proper WSGI server (Gunicorn)
7. Add HTTPS/SSL

## 💡 Tips

- Test each challenge before the event
- Monitor the leaderboard during competition
- Have backup answers ready
- Consider time limits if needed
- Prepare hints that don't give away answers
- Keep the database backed up

---

**Your Chrono Nexus Protocol CTF game is ready to deploy!** 🌌

Good luck with your ACM event! 🎮
