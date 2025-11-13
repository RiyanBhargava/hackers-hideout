# WSGI Configuration for PythonAnywhere
# Replace YOUR_USERNAME with your actual PythonAnywhere username
# This file should be configured in PythonAnywhere Web tab

import os
import sys

# Add your project directory to the sys.path
# IMPORTANT: Replace YOUR_USERNAME with your actual username
path = '/home/YOUR_USERNAME/hackers-hideout'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables for production
os.environ['DJANGO_SETTINGS_MODULE'] = 'chrono_nexus.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'YOUR_USERNAME.pythonanywhere.com'

# IMPORTANT: Generate a new secret key for production!
# You can generate one at https://djecrety.ir/
# os.environ['DJANGO_SECRET_KEY'] = 'your-new-secret-key-here'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
