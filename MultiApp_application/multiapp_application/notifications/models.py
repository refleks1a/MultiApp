from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    expiry_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)