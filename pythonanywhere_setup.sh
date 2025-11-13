# Quick Start Script for PythonAnywhere Deployment
# Static files are already in the repo, so no need to collect them!

## After uploading to PythonAnywhere, run these commands in Bash console:

# 1. Navigate to project
cd ~/hackers-hideout

# 2. Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 hackershideout

# 3. Install Django
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# NOTE: Static files are already in your repo, so collectstatic is not needed!

# 6. Set environment variables (create .env file or set in WSGI)
# For production, add these to your WSGI file or use environment variables:
# export DJANGO_DEBUG=False
# export DJANGO_ALLOWED_HOSTS=yourusername.pythonanywhere.com
# export DJANGO_SECRET_KEY=your-new-secret-key-here

echo "Setup complete! Now configure your Web app in PythonAnywhere dashboard."
