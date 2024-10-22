from django.db import models

class Problem(models.Model):
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    title = models.CharField(max_length=125)
    description = models.TextField()
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES)
    tag = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
