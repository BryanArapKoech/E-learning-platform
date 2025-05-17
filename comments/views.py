# comments/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Comment
from courses.models import Lesson # Need Lesson to link comment
from .serializers import CommentSerializer, CommentWriteSerializer
# Use the permission from courses app or create a specific one
from courses.views import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for comments on lessons.
    Accessed typically via a nested route like /api/lessons/{lesson_id}/comments/
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Allow read, require auth to post, owner to edit/delete

    def get_queryset(self):
        # Filter comments based on the lesson_pk from the URL
        lesson_pk = self.kwargs.get('lesson_pk')
        if lesson_pk:
            return Comment.objects.filter(lesson_id=lesson_pk).select_related('user')
        return Comment.objects.none() # Or all comments if not nested - adjust as needed

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentWriteSerializer
        return CommentSerializer # Use detailed serializer for list/retrieve

    def perform_create(self, serializer):
        # Automatically set the user and lesson based on request/URL
        lesson_pk = self.kwargs.get('lesson_pk')
        try:
            lesson = Lesson.objects.get(pk=lesson_pk)
        except Lesson.DoesNotExist:
             raise serializers.ValidationError("Lesson not found.") # Or return 404

        serializer.save(user=self.request.user, lesson=lesson)

    