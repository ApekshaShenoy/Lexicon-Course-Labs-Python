import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_two.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import Student

fake = Faker()

def populate(n=10):
    for i in range(n):
        name = fake.name()
        email = fake.email()
        Student.objects.get_or_create(name=name, email=email)

if __name__ == "__main__":
    populate(20)
    print("Fake data created")
