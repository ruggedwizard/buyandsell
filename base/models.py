from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.


class Product(models.Model):
    CATEGORY = (
        ('FASHION','FASHION'),
        ('ELECTRONICS AND GADGET','ELECTRONICS AND GADGET'),
        ('FASHION','FASHION'),
        ('HOME APPLIANCES', 'HOME APPLIANCES'),
        ('OTHERS','OTHERS')
    )
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    amount = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY, max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
          
class Reviews(models.Model):
    RATING = (
        ('PREFFECT','PERFECT'),
        ('GOOD','GOOD'),
        ('AVERAGE','AVERAGE'),
        ('NOT THAT BAD','NOT THAT BAD'), 
        ('VERY POOR','VERY POOR')

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    email = models.EmailField()
    rating = models.TextField(choices=RATING, max_length=50)
    comment = models.TextField()


    def __str__(self):
        return self.name 

class Profile(models.Model):
    details = models.ForeignKey(User, on_delete=CASCADE)
    profile_image = models.ImageField()
    phone_number = models.CharField(max_length=100)
    profile_address = models.CharField(max_length=500)

    def __str__(self):
        return self.details.username + " Profile Details "
