from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # To Add any extra fields here later if needed, e.g.:
    # email = models.EmailField(unique=True) # Already unique in AbstractUser by default now
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # bio = models.TextField(blank=True)

    def __str__(self):
        return self.username # Or self.email if you prefer