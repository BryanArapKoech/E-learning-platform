# elearning_project/settings.py

import os # Make sure os is imported at the top

# ... other settings ...

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
    'comments.apps.CommentConfig',
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

# Database configuration (SQLite for now)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # BASE_DIR is already defined by Django
    }
}

# --- Add these new sections at the end of the file ---

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
    # ... other settings if needed
}

# CORS settings (Change in production!)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Your React development server
    "http://127.0.0.1:3000", # Alternative for localhost
]
# Or for very early development (less secure):
# CORS_ALLOW_ALL_ORIGINS = True

# --- End of new sections ---


# Make sure TEMPLATES, STATIC_URL, etc., are still present

# Set timezone if needed
# TIME_ZONE = 'UTC'