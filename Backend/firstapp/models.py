from django.db import models
from django.utils import timezone

# from django.contrib.auth.models import User


class poll(models.Model):
    question = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.question


class options(models.Model):
    poll = models.ForeignKey(poll, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text
