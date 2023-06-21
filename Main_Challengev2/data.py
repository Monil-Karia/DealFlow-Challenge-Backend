import os
import sys
import random
import string
from faker import Faker
from django.utils import timezone

# Add the path to your Django project
sys.path.append(r'C:\Users\Monil Karia\OneDrive\Desktop\DealFlow-Challenge\Main_Challengev2')

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'Main_Challengev2.settings'

import django
django.setup()

from api.models import Freelancers, Brand

fake = Faker()

# Function to generate a random string
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate a random phone number
def random_phone_number():
    return random.randint(1000000000, 9999999999)

# Function to create and save Freelancer objects
def create_freelancers():
    brands = ["Brand 1", "Brand 2", "Brand 3", "Brand 4", "Brand 5","Brand 6", "Brand 7", "Brand 8", "Brand 9", "Brand 10"]  
    
    for i in range(1, 101):
        brand = random.choice(brands)
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = random_phone_number()
        followers = str(random.randint(100, 10000))
        added_data = fake.past_datetime(start_date='-30d', tzinfo=timezone.get_current_timezone())
        social_media = random.choice(['Instagram', 'TIK TOK', 'Twitter', 'Discord', 'Twitch'])
        
        freelancer = Freelancers(
            freelancer_id=i,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            brand=brand,
            followers=followers,
            added_data=added_data,
            social_media=social_media
        )
        freelancer.save()

if __name__ == '__main__':
    create_freelancers()
