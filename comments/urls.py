# comments/urls.py
from django.urls import path, include
from rest_framework_nested import routers
from .views import CommentViewSet

# Add code here
# We will integrate comment URLs nested under lessons
# within the main `elearning_project/urls.py` or by including `courses.urls` which
# ideally would define the comment nesting.

urlpatterns = [
    # URLs will be defined via nested routers in the main URL config or courses app config
]