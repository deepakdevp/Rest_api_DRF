from django.db import models


class Users(models.Model):

    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Company_Name = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    Zip = models.CharField(max_length=6, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Web = models.CharField(max_length=20, null=True, blank=True)
