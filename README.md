# 🌌 Chrono Nexus Protocol - CTF Game

A Django-based Capture The Flag (CTF) game where players journey through space solving cryptographic challenges to stop the rogue AI NEXUS-9 from rewriting history.

## 🎮 Game Overview

**Year 2149** — A rogue AI, NEXUS-9, is rewriting time data stored in orbital archives. Players must decode seven encrypted stations across the solar system to prevent the collapse of the historical timeline.

### Features

- **7 Progressive Challenges**: From prime numbers to complex ciphers
- **Point System**: Earn points based on challenge difficulty (100-500 points)
- **Strategic Hints**: Use hints at the cost of points
- **Leaderboard**: Compete with other players globally
- **Progress Tracking**: Track attempts, completions, and statistics
- **Space-Themed UI**: Immersive dark theme with cyberpunk aesthetics

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone or Navigate to the Project

```bash
cd c:\Users\USER\Desktop\ACM\hackers-hideout
```

### 2. Create a Virtual Environment (Recommended)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Initialize the Database

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Load Challenge Data

```powershell
python manage.py init_challenges
```

### 6. Create a Superuser (Admin)

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an admin account for accessing the Django admin panel.

### 7. Run the Development Server

```powershell
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## 🎯 How to Use

### For Players

1. **Register**: Go to `http://127.0.0.1:8000/register/` and create an account with a team name
2. **Login**: Access your dashboard at `http://127.0.0.1:8000/login/`
3. **Solve Challenges**: Progress through 7 challenges sequentially
4. **Submit Flags**: All answers must be submitted in the format `flag{answer}`
5. **Use Hints Wisely**: Hints deduct points but can help solve difficult challenges
6. **Check Leaderboard**: See how you rank against other players

### For Administrators

1. **Access Admin Panel**: Go to `http://127.0.0.1:8000/admin/`
2. **Manage Challenges**: Add, edit, or remove challenges
3. **Monitor Players**: View player progress and scores
4. **Review Submissions**: Track all submission attempts

## 🧩 Challenges Overview

| Part | Title | Difficulty | Points | Type |
|------|-------|------------|--------|------|
| 1 | The Chrono Bridge | Easy | 100 | Prime Numbers |
| 2 | The Lunar Core | Easy | 150 | Geometric Sequence |
| 3 | The Signal Fragment | Medium | 200 | Binary to ASCII |
| 4 | The Paradox Core | Medium | 250 | Pattern Recognition |
| 5 | The Void Transmission | Medium | 300 | Hex to ASCII |
| 6 | The Martian Vault | Hard | 350 | Caesar Cipher |
| 7 | The Chrono Nexus Core | Hard | 500 | Final Combination |

## 📁 Project Structure

```
hackers-hideout/
├── chrono_nexus/           # Django project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI application
├── game/                   # Main game application
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # App URL routing
│   ├── admin.py            # Admin configuration
│   └── management/         # Custom management commands
│       └── commands/
│           └── init_challenges.py
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── game/               # Game-specific templates
│       ├── home.html
│       ├── dashboard.html
│       ├── challenge.html
│       ├── leaderboard.html
│       └── profile.html
├── static/                 # Static files
│   └── css/
│       └── style.css       # Main stylesheet
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🎨 Game Mechanics

### Scoring System

- **Base Points**: Each challenge has a base point value (100-500)
- **Hint Penalty**: Using a hint deducts 10-50 points from the final score
- **One-Time Bonus**: Points are only awarded once per challenge
- **Progressive Unlock**: Challenges must be completed sequentially (except final)

### Challenge Types

1. **Mathematical Patterns**: Prime numbers, sequences
2. **Encoding/Decoding**: Binary, Hexadecimal, Caesar Cipher
3. **Logic Puzzles**: Pattern recognition
4. **Final Challenge**: Combines all previous answers

## 🔧 Configuration

### Database

By default, the project uses SQLite (`db.sqlite3`). To use PostgreSQL or MySQL:

1. Install the appropriate database adapter
2. Update `DATABASES` in `chrono_nexus/settings.py`

### Security

⚠️ **Important**: Before deploying to production:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up proper database (not SQLite)

## 📊 Admin Features

The Django admin panel provides:

- **Challenge Management**: CRUD operations on challenges
- **Player Monitoring**: View all registered players and scores
- **Submission Tracking**: Review all answers submitted
- **Hint Usage**: Monitor which players used hints

## 🐛 Troubleshooting

### Database Errors

```powershell
python manage.py migrate --run-syncdb
```

### Static Files Not Loading

```powershell
python manage.py collectstatic
```

### Reset Challenges

```powershell
python manage.py init_challenges
```

## 🎓 Educational Use

This CTF game is designed for:

- Cybersecurity education
- Coding competitions
- CTF practice events
- Computer science clubs
- Hackathons

## 📝 Answers Reference (For Admins Only)

<details>
<summary>Click to reveal answers</summary>

1. Part 1: `flag{13}`
2. Part 2: `flag{243}`
3. Part 3: `flag{LunaRim}`
4. Part 4: `flag{52}`
5. Part 5: `flag{heart_of_the_nexus}`
6. Part 6: `flag{temporal_loop}`
7. Part 7: `flag{heart_of_the_nexus_LunaRim_13_52_243_temporal_loop}`

</details>

## 🤝 Contributing

Feel free to:

- Add new challenges
- Improve the UI/UX
- Add new features (timers, teams, etc.)
- Fix bugs

## 📜 License

This project is created for educational purposes.

## 🌟 Credits

Developed for ACM Hackers Hideout CTF Event
Theme: The Chrono Nexus Protocol - Year 2149

---

**Ready to save the timeline, Agent?** 🚀
