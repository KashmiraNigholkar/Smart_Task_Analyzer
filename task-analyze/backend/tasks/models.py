# backend/tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    urgency = models.IntegerField(default=1)        # 1..5
    importance = models.IntegerField(default=1)     # 1..5
    time_required = models.FloatField(default=1.0)  # hours
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.title}"
