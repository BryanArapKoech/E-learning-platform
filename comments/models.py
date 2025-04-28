# comments/models.py
from django.db import models
from django.conf import settings
from courses.models import Lesson # Import Lesson model

class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Track edits

    class Meta:
        ordering = ['created_at'] # Show oldest comments first

    def __str__(self):
        return f"Comment by {self.user.username} on {self.lesson.title}"