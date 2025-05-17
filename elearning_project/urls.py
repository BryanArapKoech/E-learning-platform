# elearning_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers # Import nested routers here too

# Import views from apps to register directly if needed, or include app url files
from courses.views import CourseViewSet, LessonViewSet, ResourceFileViewSet
from comments.views import CommentViewSet

# --- Setup Routers ---

# Top-level router
router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

# router.register(r'lessons', LessonViewSet, basename='lesson')
# router.register(r'resources', ResourceFileViewSet, basename='resourcefile')

# Nested router for Lessons under Courses
# /api/courses/{course_pk}/lessons/
courses_router = routers.NestedDefaultRouter(router, r'courses', lookup='course')
courses_router.register(r'lessons', LessonViewSet, basename='course-lessons')

# Nested router for Resources under Lessons
# /api/courses/{course_pk}/lessons/{lesson_pk}/resources/
lessons_router = routers.NestedDefaultRouter(courses_router, r'lessons', lookup='lesson')
lessons_router.register(r'resources', ResourceFileViewSet, basename='lesson-resources')

# Nested router for Comments under Lessons
# /api/courses/{course_pk}/lessons/{lesson_pk}/comments/
lessons_router.register(r'comments', CommentViewSet, basename='lesson-comments') # Register comments here!


# --- URL Patterns ---
urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth endpoints
    path('api/users/', include('users.urls')),

    # Main API routes from routers
    path('api/', include(router.urls)),
    path('api/', include(courses_router.urls)),
    path('api/', include(lessons_router.urls)),

    # No need to include courses.urls or comments.urls separately if defined here
]

# Add media URL configuration for development (for FileFields/ImageFields later)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Add static files serving for dev if needed and not handled elsewhere
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add MEDIA_URL and MEDIA_ROOT to settings.py if not already there
# elearning_project/settings.py
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')