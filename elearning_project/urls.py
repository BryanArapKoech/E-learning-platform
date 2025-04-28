# elearning_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')), # Add this line for user auth endpoints

    # Add placeholders for other app APIs later
    # path('api/', include('courses.urls')),
    # path('api/', include('comments.urls')),
]