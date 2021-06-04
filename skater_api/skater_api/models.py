from django.db import models

# Create your models here.
class Skater(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    home_town = models.CharField(max_length=100)
    board_sponsor = models.CharField(max_length=120)
    shoe_sponsor = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Tricks(models.Model):
    trick_name = models.CharField(max_length=100)
    signature_trick = models.CharField(max_length=100)
    favorite_trick = models.CharField(max_length=120)
    trick_location = models.CharField(max_length=150)
    photo_url = models.TextField()

    def __str__(self):
        return self.trick_name

