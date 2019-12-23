from django.db import models


class Users(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
