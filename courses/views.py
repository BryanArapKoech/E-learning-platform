from django.shortcuts import render

# courses/views.py
from rest_framework import viewsets, permissions
from .models import Course, Lesson, ResourceFile
from .serializers import (
    CourseSerializer,
    CourseListSerializer,
    CourseWriteSerializer,
    LessonSerializer,
    ResourceFileSerializer
)
from .permissions import IsInstructorOrReadOnly # permission To be created

# Simple Permission: Only allow object owner (instructor) to edit/delete
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # Allow GET, HEAD, OPTIONS
            return True
        # Check if the user making the request is the owner (instructor)
        # Adjust field based on model ('instructor' for Course, maybe 'user' for others)
        if hasattr(obj, 'instructor'):
            return obj.instructor == request.user
        elif hasattr(obj, 'user'): # e.g., for Comments later
            return obj.user == request.user
        # Add checks for other ownership fields if needed
        return False

# Permission: Allow Admin/Instructor to create/edit/delete, others read-only
class IsInstructorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write access only for authenticated users who are staff/admin
        # Or potentially users marked as 'instructors' via a group or profile field later
        return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write access only for the instructor of the course or staff/admin
        # Assumes Course model has 'instructor' field
        return obj.instructor == request.user or request.user.is_staff


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().prefetch_related('lessons', 'instructor') # Optimize query
    permission_classes = [IsInstructorOrAdminOrReadOnly] # Only Staff/Admin can create/edit courses

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer # Simpler serializer for list view
        if self.action in ['create', 'update', 'partial_update']:
             return CourseWriteSerializer # Use write serializer for CUD actions
        return CourseSerializer # Default detailed serializer for retrieve

    def perform_create(self, serializer):
        # Automatically set the instructor to the logged-in user on creation
        serializer.save(instructor=self.request.user)

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lessons. Nested under courses ideally, but simple setup first.
    Filterable by course ID.
    """
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Basic permission for now
    # More specific permission: Only instructor of the course can edit lessons
    # permission_classes = [IsCourseInstructorOrReadOnly] # Custom permission needed

    def get_queryset(self):
        """Optionally filter lessons based on a query parameter"""
        queryset = Lesson.objects.all().select_related('course')
        course_id = self.request.query_params.get('course_id')
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    # TODO: Add permission check on create/update/delete to ensure user is instructor of the parent course

class ResourceFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for resource files associated with lessons.
    """
    serializer_class = ResourceFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Basic permission
    # TODO: Add permission check linked to parent lesson/course instructor

    def get_queryset(self):
        """Optionally filter resources based on a query parameter"""
        queryset = ResourceFile.objects.all().select_related('lesson')
        lesson_id = self.request.query_params.get('lesson_id')
        if lesson_id is not None:
            queryset = queryset.filter(lesson_id=lesson_id)
        return queryset
    # TODO: Add permission check on create/update/delete