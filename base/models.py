from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reviews(models.Model):
    RATING = (
        ('PREFFECT','PERFECT'),
        ('GOOD','GOOD'),
        ('AVERAGE','AVERAGE'),
        ('NOT THAT BAD','NOT THAT BAD'), 
        ('VERY POOR','VERY POOR')

    )
    name = models.TextField(max_length=200) 
    email = models.EmailField()
    rating = models.TextField(choices=RATING, max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.name + self.rating[:20]

class Product(models.Model):
    CATEGORY = (
        ('FASHION','FASHION'),
        ('ELECTRONICS AND GADGET','ELECTRONICS AND GADGET'),
        ('FASHION','FASHION'),
        ('HOME APPLIANCES', 'HOME APPLIANCES'),
        ('OTHERS','OTHERS')
    )
    posted_by = User
    name = models.CharField(max_length=200)
    # image
    amount = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY, max_length=50)
    description = models.TextField(null=True, blank=True)
    reviews = models.ForeignKey(Reviews,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name  

