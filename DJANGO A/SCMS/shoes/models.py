from django.db import models

# Create your models here.

class Shoe(models.Model):
    name=models.CharField(max_length=50)
    shoe_brand=models.CharField(max_length=50)
    country_of_manufacture=models.CharField(max_length=50)
    size=models.IntegerField()
    date_of_manufacture=models.DateField()
  


    def __str__(self):
      return f'Shoe: {self.shoe_name}{self.shoe_brand}'