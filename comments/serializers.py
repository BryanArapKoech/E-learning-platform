# comments/serializers.py
from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer # To show commenter details

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # Display user info, don't allow setting it via API directly
    lesson = serializers.PrimaryKeyRelatedField(read_only=True) # Lesson set via URL typically

    class Meta:
        model = Comment
        fields = ('id', 'lesson', 'user', 'text', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at', 'user', 'lesson')

# Serializer for creating comments where user/lesson are handled by the view
class CommentWriteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = ('text',) # Only text is needed from user input