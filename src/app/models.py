from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    discription = models.TextField(max_length=1000, null=True)     
    
    # def __str__(self):
    #     return self.name + ' ' + self.price 