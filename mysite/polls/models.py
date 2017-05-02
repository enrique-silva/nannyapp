from django.db import models

# Create your models here.

import datetime
from django.db import models
from django.utils import timezone



class User(models.Model):
    #primary key will auto generated
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Company(models.Model):
    #primary key will be auto generated
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    pay_rate = models.FloatField()
    email_address = models.EmailField()

    def __str__(self):
        return self.company_name

class Shift(models.Model):
    #primary key will be auto generated
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    shift_date = models.DateTimeField()
    #clock_out = models.DateTimeField()
    total_hours = models.FloatField()

    def __str__(self):
        return self.total_hours

class Expenses(models.Model):
    #primary key will be auto generated
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cost = models.FloatField()
    expense_date = models.DateTimeField()

    def __str__(self):
        return self.description

