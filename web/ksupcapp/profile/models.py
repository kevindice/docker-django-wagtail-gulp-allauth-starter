from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.user.username + '\'s profile'

# Each person has 0 or more phone numbers
class Phone(models.Model):
    phone_number = models.CharField(max_length=12)
    type = models.CharField(
        max_length=2,
        choices=PHONE_NUMBER_TYPE_CHOICES,
        default=CELL
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        return self.profile.user.username + '\'s ' + (self.get_type_display() + ' Phone Number').lower()
