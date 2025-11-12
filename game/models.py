from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Challenge(models.Model):
    """Represents each challenge/part in the game"""
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]
    
    part_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    story_text = models.TextField()
    challenge_text = models.TextField()
    answer = models.CharField(max_length=200)
    points = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='MEDIUM')
    hint = models.TextField(blank=True, null=True)
    hint_penalty = models.IntegerField(default=10)
    is_final = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['part_number']
    
    def __str__(self):
        return f"Part {self.part_number}: {self.title}"


class Player(models.Model):
    """Player profile linked to Django User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    total_score = models.IntegerField(default=0)
    current_challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, null=True, blank=True)
    completed_challenges = models.ManyToManyField(Challenge, through='Submission', related_name='completed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-total_score', 'created_at']
    
    def __str__(self):
        return self.team_name


class Submission(models.Model):
    """Tracks each submission attempt"""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    submitted_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.player.team_name} - Part {self.challenge.part_number} - {'✓' if self.is_correct else '✗'}"


class HintUsage(models.Model):
    """Tracks when players use hints"""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    penalty_applied = models.IntegerField()
    used_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['player', 'challenge']
        ordering = ['-used_at']
    
    def __str__(self):
        return f"{self.player.team_name} used hint for Part {self.challenge.part_number}"
