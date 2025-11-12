from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.game_dashboard, name='game_dashboard'),
    path('challenge/<int:part_number>/', views.challenge_detail, name='challenge_detail'),
    path('challenge/<int:part_number>/submit/', views.submit_answer, name='submit_answer'),
    path('challenge/<int:part_number>/hint/', views.use_hint, name='use_hint'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
]
