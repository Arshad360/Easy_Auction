from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
   
    DEFAULT_USER = 1
    name = models.CharField(max_length = 100, blank = False)
    description = models.CharField(max_length = 200, blank = False)
    minimum_bid_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    user = models.ForeignKey(User, blank = False, on_delete = models.CASCADE, default = DEFAULT_USER)
    image = models.ImageField(default = 'None/NIA.png')
    auction_end_date_time = models.CharField(max_length=10)
    created = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - starts at ${self.initial}"