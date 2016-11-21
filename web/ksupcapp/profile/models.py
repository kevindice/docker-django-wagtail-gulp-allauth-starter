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

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


    def __str__(self):
        return self.person.user.username + '\'s ' + (self.get_type_display() + ' Phone Number').lower()
