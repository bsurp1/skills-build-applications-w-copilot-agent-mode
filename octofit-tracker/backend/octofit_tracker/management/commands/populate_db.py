from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team=marvel.name, is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team=marvel.name, is_superhero=True),
            User(email='batman@dc.com', name='Batman', team=dc.name, is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date='2025-10-01'),
            Activity(user=users[1], type='Cycling', duration=45, date='2025-10-02'),
            Activity(user=users[2], type='Swimming', duration=60, date='2025-10-03'),
            Activity(user=users[3], type='Yoga', duration=50, date='2025-10-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workouts = [
            Workout(name='HIIT', description='High Intensity Interval Training', difficulty='Hard'),
            Workout(name='Cardio', description='Cardio workout', difficulty='Medium'),
            Workout(name='Strength', description='Strength training', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
