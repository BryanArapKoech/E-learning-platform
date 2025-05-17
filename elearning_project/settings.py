# elearning_project/settings.py

import os 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret! generate a real secret key for production. For development, this is okay.
SECRET_KEY = 'django-insecure-=your-default-key-here-if-you-remember-it-or-make-one-up-for-now'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set this to True for development. A PERSONAL REMINDER

ALLOWED_HOSTS = [] 


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps (will add more here)
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # Your apps
    'users.apps.UsersConfig',
    'courses.apps.CoursesConfig',
    'comments.apps.CommentsConfig',
]

MIDDLEWARE = [
    # Add CorsMiddleware near the top, before CommonMiddleware if possible
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# 
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Creates a 'media' folder in project root

# Database configuration (SQLite???)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}



# Specify the custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Add SessionAuthentication if you want to use the browsable API login
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # Default to read-only for anonymous users, require auth for modifications
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

# Simple JWT settings (optional: customize token lifetimes)
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), # Adjust as needed
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    
}

# CORS settings (To change in production!)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Your React development server
    "http://127.0.0.1:3000", # Alternative for localhost
]
