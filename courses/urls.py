# courses/urls.py
from django.urls import path, include
from rest_framework_nested import routers # Use nested routers for lessons/resources under courses
from .views import CourseViewSet, LessonViewSet, ResourceFileViewSet

# Top-level router for Courses
router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

# Nested router for Lessons within a Course
# URL Pattern: /api/courses/{course_pk}/lessons/
courses_router = routers.NestedDefaultRouter(router, r'courses', lookup='course')
courses_router.register(r'lessons', LessonViewSet, basename='course-lessons')

# Nested router for Resources within a Lesson (which is within a Course)
# URL Pattern: /api/courses/{course_pk}/lessons/{lesson_pk}/resources/
lessons_router = routers.NestedDefaultRouter(courses_router, r'lessons', lookup='lesson')
lessons_router.register(r'resources', ResourceFileViewSet, basename='lesson-resources')


# We might need non-nested routes for lessons/resources if accessed directly
# simple_router = routers.DefaultRouter()
# simple_router.register(r'lessons', LessonViewSet, basename='lesson') # Needs modification in queryset logic
# simple_router.register(r'resources', ResourceFileViewSet, basename='resourcefile')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(courses_router.urls)),
    path('', include(lessons_router.urls)),
    # path('', include(simple_router.urls)), # Uncomment if direct access needed
]