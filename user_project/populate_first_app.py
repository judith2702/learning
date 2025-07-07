import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_project.settings')
django.setup()

from users_app.models import User

fake = Faker()

def populate(n=10):
    for _ in range(n):
        first = fake.first_name()
        last = fake.last_name()
        email = fake.email()
        User.objects.get_or_create(first_name=first, last_name=last, email=email)

if __name__ == "__main__":
    populate(20)
    print("Successfully populated database with fake users.")
