import os
import sys
import random
from faker import Faker
from django.utils import timezone

# Add the path to your Django project
sys.path.append(r'C:\Users\Monil Karia\OneDrive\Desktop\DealFlow-Challenge\Main_Challengev2')

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'Main_Challengev2.settings'

import django
django.setup()

from api.models import Brand, Freelancers

fake = Faker()

# Function to create and save Brand objects
def create_brands():
    freelancers = Freelancers.objects.all()  # Retrieve all Freelancer objects from the database
    
    for i in range(1, 101):
        brand_name = f"Brand {i}"
        about = fake.sentence(nb_words=10)
        
        # Select a random Freelancer object from the list
        freelancer = random.choice(freelancers)
        
        brand = Brand(
            brand_id=i,
            brand_name=brand_name,
            about=about,
            freelancers=freelancer  # Assign the Freelancer object to the 'freelancers' field
        )
        brand.save()

if __name__ == '__main__':
    create_brands()
