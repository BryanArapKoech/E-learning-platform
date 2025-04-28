from django.db import models

# courses/models.py
from django.db import models
from django.conf import settings # To link to AUTH_USER_MODEL

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Or PROTECT, CASCADE depending on requirements
        null=True, # Allow courses without instructors? Or make required?
        related_name='courses_taught'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # thumbnail = models.ImageField(upload_to='course_thumbnails/', null=True, blank=True) # Add later

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0) # For ordering lessons within a course
    video_url = models.URLField(blank=True, null=True) # For YouTube/Vimeo links initially
    # video_file = models.FileField(upload_to='lesson_videos/', null=True, blank=True) # For self-hosting later
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at'] # Default ordering

    def __str__(self):
        return f"{self.course.title} - Lesson {self.order}: {self.title}"

class ResourceFile(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='resources', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='lesson_resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} for Lesson: {self.lesson.title}"
