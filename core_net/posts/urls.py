from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('post/create', PostCreateView.as_view(), namespace="post-create"),
]
