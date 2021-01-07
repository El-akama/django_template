from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from dateutil.relativedelta import relativedelta



class CustomUser(AbstractUser):
    """Django User Model that come with:
    username, first_name, last_name, email, password, ...."""

    gender = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def age(self):
        if self.date_of_birth == None:
            return None
        age = relativedelta(date.today(), self.date_of_birth)
        return age.years

        