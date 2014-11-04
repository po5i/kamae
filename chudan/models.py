from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)    
    genre = models.CharField(max_length=1,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50,blank=True,null=True)
    education_leven = models.CharField(max_length=200,blank=True,null=True)
    working = models.NullBooleanField()
    birth_date = models.DateField(blank=True,null=True)
    kendo_register_date = models.DateField(blank=True,null=True)

class Status(models.Model):
    user = models.ForeignKey(User)
    status_name = models.CharField(max_length=50)
    reason = models.TextField(blank=True,null=True)
    timestamp = models.DateField(auto_now_add=True)

class Attendance(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateField()  #month and year only matters
    percentage = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)

class Rank(models.Model):
    user = models.ForeignKey(User)
    examination_date = models.DateField()
    approved = models.BooleanField(default=True)

class Championship(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    keyname = models.CharField(max_length=50,blank=True,null=True)
    individual = models.NullBooleanField()
    team = models.NullBooleanField()
    wins = models.IntegerField(blank=True,null=True)
    losses = models.IntegerField(blank=True,null=True)

class Travel(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    keyname = models.CharField(max_length=50,blank=True,null=True)
    examination = models.NullBooleanField()
    championship = models.NullBooleanField()
    seminar = models.NullBooleanField()
    gasshuku = models.NullBooleanField()