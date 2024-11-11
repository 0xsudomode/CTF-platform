from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('pwn', 'Pwn'),
        ('rev', 'Reverse Engineering'),
        ('crypto', 'Cryptography'),
        ('web', 'Web Exploitation'),
        ('misc', 'Miscellaneous'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.IntegerField(default=1)  # 1 for easy, 5 for hard
    flag = models.CharField(max_length=200)  # The flag to be submitted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Scoreboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    solved_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=100)  # Points awarded for solving

    def __str__(self):
        return f"{self.user.username} solved {self.challenge.title}"
