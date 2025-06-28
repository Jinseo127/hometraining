# models.py (in your reportmanagement app)

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    attempts = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
