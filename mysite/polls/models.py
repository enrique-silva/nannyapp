from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class User(models.Model):
    # primary key will auto generated
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Employer(models.Model):
    # primary key will be auto generated
    company_name = models.CharField(max_length=30)
    email_address = models.EmailField()

    def __str__(self):
        return self.company_name


class Expense(models.Model):
    # primary key will be auto generated
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    pay_rate = models.FloatField()
    additional_cost = models.FloatField()
    shift_date = models.DateField()
    total_hours = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.total_hours


class Invoice(models.Model):
    c_name = models.ForeignKey(Employer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

