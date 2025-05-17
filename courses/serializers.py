# courses/serializers.py
from rest_framework import serializers
from .models import Course, Lesson, ResourceFile
from users.serializers import UserSerializer # To show instructor details

class ResourceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = ('id', 'name', 'file', 'uploaded_at')

class LessonSerializer(serializers.ModelSerializer):
    resources = ResourceFileSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'content', 'order', 'video_url', 'resources', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class CourseSerializer(serializers.ModelSerializer):
    # Simple instructor display (read-only)
    instructor = UserSerializer(read_only=True)
    # List lessons associated with the course (read-only in this view)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'instructor', 'lessons', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

# We might need a separate simpler serializer for listing courses without lessons
class CourseListSerializer(serializers.ModelSerializer):
     instructor = UserSerializer(read_only=True)
     class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'instructor', 'created_at') # Fewer fields for list view


# Serializer for creating/updating courses where instructor is set automatically
class CourseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description') # Instructor set in view