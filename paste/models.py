from django.db import models
from django.contrib.auth.models import User


class Paste(models.Model):
    title = models.CharField(max_length=50)
    paste = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pastes')

    class Meta:
        ordering = ['-created']
