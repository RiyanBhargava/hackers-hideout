# Deploy Hacker's Hideout to PythonAnywhere

## Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com/
2. Sign up for a free Beginner account
3. Verify your email

## Step 2: Upload Your Code to GitHub (Recommended)

### Option A: Using GitHub (Recommended)
1. Create a new repository on GitHub
2. In your local terminal, run:
```bash
cd "c:\Users\riyan\OneDrive\Desktop\hackers-hideout\hackers-hideout"
git init
git add .
git commit -m "Initial commit - Hacker's Hideout"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hackers-hideout.git
git push -u origin main
```

### Option B: Upload Files Directly
- Use PythonAnywhere's file upload feature (slower for many files)

## Step 3: Setup on PythonAnywhere

### 3.1 Open a Bash Console
1. Log in to PythonAnywhere
2. Click on "Consoles" tab
3. Start a new "Bash" console

### 3.2 Clone Your Project
In the Bash console, run:
```bash
# If using GitHub:
git clone https://github.com/YOUR_USERNAME/hackers-hideout.git
cd hackers-hideout

# Or navigate to uploaded files:
cd hackers-hideout
```

### 3.3 Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 hackershideout
```

### 3.4 Install Dependencies
```bash
pip install django
```

### 3.5 Setup Database
```bash
python manage.py migrate
python manage.py createsuperuser
# Follow prompts to create admin user
```

### 3.6 Collect Static Files
```bash
python manage.py collectstatic --noinput
```

## Step 4: Configure Web App

### 4.1 Create Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration" (not Django wizard)
4. Select Python 3.10

### 4.2 Configure Virtual Environment
In the "Virtualenv" section:
- Enter: `/home/YOUR_USERNAME/.virtualenvs/hackershideout`

### 4.3 Configure WSGI File
1. Click on the WSGI configuration file link
2. Delete all content and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/hackers-hideout'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'chrono_nexus.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 4.4 Configure Static Files
In the "Static files" section, add:

| URL          | Directory                                              |
|--------------|--------------------------------------------------------|
| /static/     | /home/YOUR_USERNAME/hackers-hideout/staticfiles       |

## Step 5: Update Django Settings

In PythonAnywhere Bash console, edit settings.py:
```bash
nano chrono_nexus/settings.py
```

Update:
```python
DEBUG = False
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']
```

Save: Ctrl+X, Y, Enter

## Step 6: Reload Web App
1. Go to "Web" tab
2. Click the green "Reload" button
3. Visit: https://YOUR_USERNAME.pythonanywhere.com

## Step 7: Initialize Challenges (Optional)
If you have a management command to initialize challenges:
```bash
python manage.py init_challenges
```

## Troubleshooting

### Check Error Logs
1. Go to "Web" tab
2. Click on error log link
3. Check for errors

### Common Issues

**Issue: 502 Bad Gateway**
- Check WSGI file path is correct
- Verify virtual environment path
- Check error logs

**Issue: Static files not loading**
- Run `python manage.py collectstatic`
- Verify static files mapping in Web tab
- Check STATIC_ROOT in settings.py

**Issue: Database errors**
- Run migrations: `python manage.py migrate`
- Check database file permissions

### Database Location
Your SQLite database will be at:
```
/home/YOUR_USERNAME/hackers-hideout/db.sqlite3
```

## Security Notes

1. **SECRET_KEY**: Change it to a new random string in production
2. **DEBUG**: Set to False in production
3. **ALLOWED_HOSTS**: Only include your PythonAnywhere domain
4. **Database Backups**: Regularly backup your db.sqlite3 file

## Updating Your App

When you make changes:
```bash
# In PythonAnywhere Bash console
cd hackers-hideout
git pull origin main  # If using Git
python manage.py migrate  # If database changed
python manage.py collectstatic --noinput  # If static files changed
# Then reload web app from Web tab
```

## Free Account Limitations
- One web app
- Custom domain not included (use YOUR_USERNAME.pythonanywhere.com)
- App sleeps after 3 months of inactivity
- Limited CPU time

## Need Help?
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- PythonAnywhere Help: https://help.pythonanywhere.com/
