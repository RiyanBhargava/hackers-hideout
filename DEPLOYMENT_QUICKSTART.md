# 🔐 Hacker's Hideout - PythonAnywhere Deployment Guide

## Quick Deployment Steps

### 1️⃣ Push to GitHub
```bash
cd "c:\Users\riyan\OneDrive\Desktop\hackers-hideout\hackers-hideout"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hackers-hideout.git
git push -u origin main
```

### 2️⃣ PythonAnywhere Setup
1. Sign up at https://www.pythonanywhere.com (free account)
2. Open a **Bash console**
3. Run:
```bash
git clone https://github.com/YOUR_USERNAME/hackers-hideout.git
cd hackers-hideout
mkvirtualenv --python=/usr/bin/python3.10 hackershideout
pip install django
python manage.py migrate
python manage.py createsuperuser
```

**Note**: Since staticfiles are already in your repo, you don't need to run collectstatic!

### 3️⃣ Configure Web App
1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration** → **Python 3.10**
3. Set **Virtualenv**: `/home/YOUR_USERNAME/.virtualenvs/hackershideout`
4. Edit **WSGI file** (click on the link), delete all and paste:

```python
import os
import sys

path = '/home/YOUR_USERNAME/hackers-hideout'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'chrono_nexus.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'YOUR_USERNAME.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. Add **Static files** mapping:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/hackers-hideout/staticfiles`

### 4️⃣ Launch! 🚀
1. Click the green **Reload** button
2. Visit: `https://YOUR_USERNAME.pythonanywhere.com`
3. Admin panel: `https://YOUR_USERNAME.pythonanywhere.com/admin`

## 📝 Notes
- Replace `YOUR_USERNAME` with your PythonAnywhere username everywhere
- Free account limitations: 1 web app, sleeps after 3 months inactivity
- Static files are already in your repo, making deployment easier!
- For detailed guide, see `PYTHONANYWHERE_DEPLOYMENT.md`

## 🔄 Updating Your Site
```bash
cd ~/hackers-hideout
git pull
python manage.py migrate  # Only if database changed
# No need to run collectstatic since it's in the repo!
# Then reload from Web tab
```

## 🆘 Troubleshooting
- **502 Error**: Check error log in Web tab
- **Static files not loading**: Verify static files mapping
- **Database errors**: Run `python manage.py migrate`

Good luck! 🎯
