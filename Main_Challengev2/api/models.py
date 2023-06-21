from django.db import models

# Create your models here.

# Model for Freelancers
class Freelancers(models.Model):
    freelancer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    brand = models.CharField(max_length=50)
    followers = models.CharField(max_length=50)
    added_data = models.DateTimeField(auto_now=True)
    social_media = models.CharField(
        max_length=50,
        choices=(
            ('Instagram', 'Instagram'),
            ('TIK TOK', 'Tik-Tok'), 
            ('Twitter', 'Twitter'),
            ('Discord', 'Discord'),
            ('Twitch', 'Twitch'),
        ),
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Model for Brand
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.brand_name

    # Defining the relation between Brand and Freelancer for more robustness
    # Foreign key relationship with Freelancers model
    freelancers = models.ForeignKey(Freelancers, on_delete=models.CASCADE, related_name='brands')
