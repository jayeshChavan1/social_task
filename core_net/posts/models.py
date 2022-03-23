from django.db import models
from django.contrib.humanize.templatetags import humanize
from accounts.models import User
from django.utils.timezone import now


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    created_at = models.DateTimeField(default=now)

    def get_date(self):
        return humanize.naturaltime(self.created_at)