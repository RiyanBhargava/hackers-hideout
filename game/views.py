from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Challenge, Player, Submission, HintUsage
import re


def normalize_answer(answer):
    """Normalize answer format for comparison"""
    # Extract content between flag{} brackets
    match = re.match(r'flag\{(.+)\}', answer.strip().lower())
    if match:
        return match.group(1)
    return answer.strip().lower()


def home(request):
    """Landing page"""
    if request.user.is_authenticated:
        return redirect('game_dashboard')
    return render(request, 'game/home.html')


def register(request):
    """Player registration"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        team_name = request.POST.get('team_name')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        first_challenge = Challenge.objects.filter(part_number=1).first()
        player = Player.objects.create(
            user=user,
            team_name=team_name,
            current_challenge=first_challenge
        )
        
        login(request, user)
        messages.success(request, f'Welcome to the Chrono Nexus Protocol, {team_name}!')
        return redirect('game_dashboard')
    
    return render(request, 'game/register.html')


def user_login(request):
    """Player login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back, Agent!')
            return redirect('game_dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
    
    return render(request, 'game/login.html')


def user_logout(request):
    """Player logout"""
    logout(request)
    messages.success(request, 'You have been logged out. Stay vigilant, Agent.')
    return redirect('home')


@login_required
def game_dashboard(request):
    """Main game dashboard"""
    player = get_object_or_404(Player, user=request.user)
    
    # Get all challenges
    all_challenges = Challenge.objects.all()
    
    # Get completed challenge IDs
    completed_ids = Submission.objects.filter(
        player=player,
        is_correct=True
    ).values_list('challenge_id', flat=True)
    
    # Get hints used
    hints_used = HintUsage.objects.filter(player=player).values_list('challenge_id', flat=True)
    
    context = {
        'player': player,
        'challenges': all_challenges,
        'completed_ids': list(completed_ids),
        'hints_used': list(hints_used),
    }
    
    return render(request, 'game/dashboard.html', context)


@login_required
def challenge_detail(request, part_number):
    """View individual challenge"""
    player = get_object_or_404(Player, user=request.user)
    challenge = get_object_or_404(Challenge, part_number=part_number)
    
    # Check if challenge is accessible
    if part_number > 1:
        previous_challenge = Challenge.objects.filter(part_number=part_number - 1).first()
        if previous_challenge:
            is_previous_completed = Submission.objects.filter(
                player=player,
                challenge=previous_challenge,
                is_correct=True
            ).exists()
            
            if not is_previous_completed and not challenge.is_final:
                messages.warning(request, 'Complete the previous challenge first!')
                return redirect('game_dashboard')
    
    # Get submission history for this challenge
    submissions = Submission.objects.filter(
        player=player,
        challenge=challenge
    ).order_by('-submitted_at')[:5]
    
    # Check if already completed
    is_completed = Submission.objects.filter(
        player=player,
        challenge=challenge,
        is_correct=True
    ).exists()
    
    # Check if hint was used
    hint_used = HintUsage.objects.filter(player=player, challenge=challenge).exists()
    
    context = {
        'player': player,
        'challenge': challenge,
        'submissions': submissions,
        'is_completed': is_completed,
        'hint_used': hint_used,
    }
    
    return render(request, 'game/challenge.html', context)


@login_required
def submit_answer(request, part_number):
    """Submit answer for a challenge"""
    if request.method != 'POST':
        return redirect('challenge_detail', part_number=part_number)
    
    player = get_object_or_404(Player, user=request.user)
    challenge = get_object_or_404(Challenge, part_number=part_number)
    
    submitted_answer = request.POST.get('answer', '').strip()
    
    # Normalize both answers for comparison
    normalized_submitted = normalize_answer(submitted_answer)
    normalized_correct = normalize_answer(challenge.answer)
    
    is_correct = (normalized_submitted == normalized_correct)
    
    # Calculate points
    points_earned = 0
    if is_correct:
        # Check if already completed
        already_completed = Submission.objects.filter(
            player=player,
            challenge=challenge,
            is_correct=True
        ).exists()
        
        if not already_completed:
            # Give full points - hint penalty was already deducted
            points_earned = challenge.points
            
            # Update player score
            player.total_score += points_earned
            
            # Update current challenge to next one
            next_challenge = Challenge.objects.filter(part_number=part_number + 1).first()
            if next_challenge:
                player.current_challenge = next_challenge
            
            player.save()
            
            # Check if hint was used for display message
            hint_usage = HintUsage.objects.filter(player=player, challenge=challenge).first()
            if hint_usage:
                messages.success(request, f'Correct! You earned {points_earned} points! (Hint penalty of {hint_usage.penalty_applied} was already deducted)')
            else:
                messages.success(request, f'Correct! You earned {points_earned} points!')
        else:
            messages.info(request, 'You already completed this challenge!')
    else:
        messages.error(request, 'Incorrect answer. Try again!')
    
    # Record submission
    Submission.objects.create(
        player=player,
        challenge=challenge,
        submitted_answer=submitted_answer,
        is_correct=is_correct,
        points_earned=points_earned
    )
    
    return redirect('challenge_detail', part_number=part_number)


@login_required
def use_hint(request, part_number):
    """Unlock hint for a challenge"""
    player = get_object_or_404(Player, user=request.user)
    challenge = get_object_or_404(Challenge, part_number=part_number)
    
    # Check if hint already used
    if HintUsage.objects.filter(player=player, challenge=challenge).exists():
        messages.info(request, 'You already used the hint for this challenge.')
        return redirect('challenge_detail', part_number=part_number)
    
    # Check if already completed
    is_completed = Submission.objects.filter(
        player=player,
        challenge=challenge,
        is_correct=True
    ).exists()
    
    if is_completed:
        messages.info(request, 'You already completed this challenge!')
        return redirect('challenge_detail', part_number=part_number)
    
    # Check if player has enough points
    if player.total_score < challenge.hint_penalty:
        messages.error(request, f'Not enough points! You need {challenge.hint_penalty} points to use this hint. Current score: {player.total_score}')
        return redirect('challenge_detail', part_number=part_number)
    
    # Deduct points immediately
    player.total_score -= challenge.hint_penalty
    player.save()
    
    # Create hint usage record
    HintUsage.objects.create(
        player=player,
        challenge=challenge,
        penalty_applied=challenge.hint_penalty
    )
    
    messages.warning(request, f'Hint unlocked! {challenge.hint_penalty} points deducted. Current score: {player.total_score}')
    
    return redirect('challenge_detail', part_number=part_number)


@login_required
def leaderboard(request):
    """Display leaderboard"""
    players = Player.objects.all().order_by('-total_score', 'created_at')[:50]
    
    context = {
        'players': players,
    }
    
    return render(request, 'game/leaderboard.html', context)


@login_required
def profile(request):
    """Player profile"""
    player = get_object_or_404(Player, user=request.user)
    
    # Get all submissions
    submissions = Submission.objects.filter(player=player).order_by('-submitted_at')[:10]
    
    # Get statistics
    total_attempts = Submission.objects.filter(player=player).count()
    correct_attempts = Submission.objects.filter(player=player, is_correct=True).count()
    hints_used = HintUsage.objects.filter(player=player).count()
    
    context = {
        'player': player,
        'submissions': submissions,
        'total_attempts': total_attempts,
        'correct_attempts': correct_attempts,
        'hints_used': hints_used,
    }
    
    return render(request, 'game/profile.html', context)
