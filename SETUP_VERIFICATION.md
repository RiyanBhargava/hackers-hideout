# 🎯 Setup Verification Checklist

Run through this checklist to ensure everything is working correctly.

## ✅ Pre-Setup Verification

- [ ] Python 3.8+ installed (`python --version`)
- [ ] pip is available (`pip --version`)
- [ ] You're in the project directory

## ✅ Setup Steps

### 1. Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
- [ ] Virtual environment created
- [ ] Virtual environment activated (you should see `(venv)` in terminal)

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```
- [ ] Django installed successfully
- [ ] No error messages

### 3. Database Setup
```powershell
python manage.py makemigrations
python manage.py migrate
```
- [ ] Migrations created for 'game' app
- [ ] All migrations applied
- [ ] `db.sqlite3` file created

### 4. Load Challenge Data
```powershell
python manage.py init_challenges
```
- [ ] See 7 "Created" or "Updated" messages
- [ ] Success message appears

### 5. Create Admin
```powershell
python manage.py createsuperuser
```
- [ ] Entered username
- [ ] Entered email (optional)
- [ ] Entered password
- [ ] Superuser created successfully

### 6. Start Server
```powershell
python manage.py runserver
```
- [ ] Server starts without errors
- [ ] See "Starting development server at http://127.0.0.1:8000/"
- [ ] No error messages in console

## ✅ Functionality Tests

### Test 1: Home Page
- [ ] Open http://127.0.0.1:8000/
- [ ] See "CHRONO NEXUS PROTOCOL" title
- [ ] See "Begin Mission" and "Resume Mission" buttons
- [ ] CSS styling loads (dark theme, cyan colors)

### Test 2: Registration
- [ ] Click "Begin Mission" or go to `/register/`
- [ ] Form displays correctly
- [ ] Can fill in username, email, team name, password
- [ ] Submit creates account
- [ ] Redirects to dashboard

### Test 3: Dashboard
- [ ] See all 7 challenges listed
- [ ] Part 1 shows "Enter Station" button
- [ ] Other parts show "🔒 Complete previous station"
- [ ] Score shows 0
- [ ] Team name displays correctly

### Test 4: Challenge 1
- [ ] Click "Enter Station" on Part 1
- [ ] See story text about the Chrono Bridge
- [ ] See challenge text with sequence: 2, 3, 5, 7, 11, ?, 19
- [ ] See hint button (💡 Use Hint)
- [ ] See answer input field
- [ ] See submit button

### Test 5: Answer Submission
- [ ] Submit wrong answer (e.g., `flag{12}`)
- [ ] See error message "Incorrect answer"
- [ ] Submit correct answer: `flag{13}`
- [ ] See success message with points earned
- [ ] Challenge marked as completed
- [ ] Score updated to 100

### Test 6: Hint System
- [ ] Go to Part 2 (unlocked after Part 1)
- [ ] Click "Use Hint" button
- [ ] Hint displays
- [ ] Warning message shows penalty
- [ ] Complete challenge
- [ ] Points = 150 - 15 = 135 added to score

### Test 7: Leaderboard
- [ ] Click "Leaderboard" in navigation
- [ ] See your team name listed
- [ ] Score shows correctly
- [ ] Progress shows X/7 challenges
- [ ] Your row highlighted

### Test 8: Profile
- [ ] Click "Profile" in navigation
- [ ] See team name and score
- [ ] See statistics (attempts, success rate, etc.)
- [ ] See recent submissions list

### Test 9: Admin Panel
- [ ] Logout from player account
- [ ] Go to `/admin/`
- [ ] Login with superuser credentials
- [ ] See Django admin interface
- [ ] Click "Challenges" - see all 7 parts
- [ ] Click "Players" - see your test account
- [ ] Click "Submissions" - see your answers
- [ ] Click "Hint usages" - see any hints used

### Test 10: Final Challenge
- [ ] Complete all 6 challenges (answers below)
- [ ] Part 7 becomes accessible
- [ ] Read the combination instructions
- [ ] Submit the final answer
- [ ] Game completes successfully

## 📝 Quick Test Answers

For rapid testing:

1. Part 1: `flag{13}`
2. Part 2: `flag{243}`
3. Part 3: `flag{LunaRim}`
4. Part 4: `flag{52}`
5. Part 5: `flag{heart_of_the_nexus}`
6. Part 6: `flag{temporal_loop}`
7. Part 7: `flag{heart_of_the_nexus_LunaRim_13_52_243_temporal_loop}`

## 🐛 Troubleshooting

### CSS Not Loading?
- Check that `/static/css/style.css` exists
- Hard refresh browser (Ctrl+F5)
- Clear browser cache

### Database Errors?
```powershell
Remove-Item db.sqlite3
python manage.py migrate
python manage.py init_challenges
```

### Import Errors?
```powershell
pip install django --upgrade
```

### Port Already in Use?
```powershell
python manage.py runserver 8080
```

### Challenges Not Loading?
```powershell
python manage.py init_challenges
```

### Admin Can't Login?
```powershell
python manage.py createsuperuser
```

## ✅ Production Readiness

Before deploying to production:

- [ ] Change SECRET_KEY in settings.py
- [ ] Set DEBUG = False
- [ ] Update ALLOWED_HOSTS
- [ ] Use PostgreSQL/MySQL instead of SQLite
- [ ] Set up static file serving
- [ ] Configure HTTPS/SSL
- [ ] Set up proper logging
- [ ] Create backups
- [ ] Test all security features

## 🎉 Success Criteria

You should be able to:

✅ Register a new account
✅ See all 7 challenges
✅ Submit answers and earn points
✅ Use hints (with penalties)
✅ View leaderboard
✅ See your profile
✅ Access admin panel
✅ Manage challenges through admin

## 📞 Support

If you encounter issues:

1. Check the error message in terminal
2. Check browser console (F12)
3. Review the README.md
4. Check Django version: `python -m django --version`
5. Verify all files exist

## 🚀 Ready to Launch!

Once all checkboxes are marked:

**Your Chrono Nexus Protocol CTF is ready for players!** 🌌

Good luck with your event! 🎮
