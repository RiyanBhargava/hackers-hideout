from django.contrib import admin
from .models import Challenge, Player, Submission, HintUsage


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['part_number', 'title', 'difficulty', 'points', 'hint_penalty', 'is_final']
    list_filter = ['difficulty', 'is_final']
    search_fields = ['title', 'question']
    ordering = ['part_number']
    fields = ['part_number', 'title', 'question', 'answer', 'hint', 'points', 'difficulty', 'hint_penalty', 'is_final']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'total_score', 'current_challenge', 'created_at']
    list_filter = ['created_at']
    search_fields = ['team_name', 'user__username']
    ordering = ['-total_score', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['player', 'challenge', 'is_correct', 'points_earned', 'submitted_at']
    list_filter = ['is_correct', 'submitted_at', 'challenge']
    search_fields = ['player__team_name', 'submitted_answer']
    ordering = ['-submitted_at']
    readonly_fields = ['submitted_at']


@admin.register(HintUsage)
class HintUsageAdmin(admin.ModelAdmin):
    list_display = ['player', 'challenge', 'penalty_applied', 'used_at']
    list_filter = ['used_at', 'challenge']
    search_fields = ['player__team_name']
    ordering = ['-used_at']
    readonly_fields = ['used_at']
