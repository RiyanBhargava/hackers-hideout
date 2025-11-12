# Create tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Challenge, Player, Submission, HintUsage


class ChallengeModelTest(TestCase):
    def setUp(self):
        self.challenge = Challenge.objects.create(
            part_number=1,
            title='Test Challenge',
            description='Test Description',
            story_text='Test Story',
            challenge_text='Test Challenge Text',
            answer='flag{test}',
            points=100,
            difficulty='EASY'
        )

    def test_challenge_creation(self):
        self.assertEqual(self.challenge.part_number, 1)
        self.assertEqual(self.challenge.points, 100)
        self.assertEqual(str(self.challenge), 'Part 1: Test Challenge')


class PlayerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.player = Player.objects.create(
            user=self.user,
            team_name='Test Team'
        )

    def test_player_creation(self):
        self.assertEqual(self.player.team_name, 'Test Team')
        self.assertEqual(self.player.total_score, 0)
        self.assertEqual(str(self.player), 'Test Team')
