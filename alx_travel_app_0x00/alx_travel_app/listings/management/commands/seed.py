from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create a superuser or guest if none exists
        if not User.objects.filter(username="host1").exists():
            host = User.objects.create_user(username="host1", password="password123")
        else:
            host = User.objects.get(username="host1")

        # Seed 10 sample listings
        for i in range(1, 11):
            Listing.objects.create(
                title=f"Sample Listing {i}",
                description="This is a sample listing for testing.",
                price=random.randint(50, 500),
                location=f"City {i}",
                host=host
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))
