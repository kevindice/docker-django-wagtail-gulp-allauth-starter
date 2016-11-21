from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

HOME='HP'
CELL='CP'
WORK='WP'
OTHER='OP'
PHONE_NUMBER_TYPE_CHOICES = (
    (HOME, 'Home'),
    (CELL, 'Cell'),
    (WORK, 'Work'),
    (OTHER, 'Other')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()

# Each person has 0 or more phone numbers
class Phone(models.Model):
    phone_number = PhoneNumberField()
    type = models.CharField(
        max_length=2,
        choices=PHONE_NUMBER_TYPE_CHOICES,
        default=CELL
    )
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username + '\'s Profile'
