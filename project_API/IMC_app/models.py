from django.db import models

# Create your models here.
class Company(models.Model):
  name=models.CharField(max_length=50)
  website=models.URLField(max_length=100)
  foundation=models.PositiveIntegerField()

class IMC(models.Model):
  genre=models.CharField(max_length=100)
  name=models.CharField(max_length=50)
  lastname=models.CharField(max_length=50)
  email=models.EmailField(max_length=100)
  weight=models.PositiveIntegerField()
  height=models.DecimalField(max_digits=5, decimal_places=2)
