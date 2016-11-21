from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

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
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username + '\'s profile'

# Each person has 0 or more phone numbers
class Phone(models.Model):
    phone_number = models.CharField(
        max_length=12,
        help_text="The format <em>xxx-xxx-xxxx</em> is preferred."
    )
    type = models.CharField(
        max_length=2,
        choices=PHONE_NUMBER_TYPE_CHOICES,
        default=CELL,
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


    def __str__(self):
        return self.person.user.username + '\'s ' + (self.get_type_display() + ' Phone Number').lower()

class JumperProfile(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    uspa_number = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True,
        validators=[
            MaxValueValidator(1000000, message="I don't believe USPA numbers exist that are that high."),
        ]
    )
    uspa_expiration_date = models.DateField(
        null=True,
        blank=True,
    )
    weight = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(50, message="I'm calling bullshit.  You weigh more than that."),
            MaxValueValidator(400, message="Let's talk about bowling.")
        ]
    )
    number_of_skydives = models.PositiveSmallIntegerField(
        default=0,
    )
    number_of_skydives_here = models.PositiveSmallIntegerField(
        default=0,
    )
    last_jump_date = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.person.user.username

class Rating(models.Model):
    jumper = models.ForeignKey(
        JumperProfile,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=5,
        choices=(
            ('Coach', (
                ('C', 'Coach'),
            )),
            ('Instructor', (
                ('SLI', 'Static Line Instructor'),
                ('IADI', 'Instructor Assisted Deployment Instructor'),
                ('AFFI', 'Accelerated Free Fall Instructor'),
                ('TI', 'Tandem Instructor'),
            )),
            ('Instructor Examiner', (
                ('CIE', 'Coach Examiner'),
                ('SLIE', 'Static Line Instructor Examiner'),
                ('IADIE', 'Instructor Assisted Deployment Instructor'),
                ('AFFI', 'Accelerated Free Fall Instructor'),
                ('TIE', 'Tandem Instructor Examiner'),
            )),
            ('Safety and Training Advisor', (
                ('STA', 'Safety and Training Advisor'),
            )),
            ('Pro', (
                ('PRO', 'Pro'),
            ))
        )
    )
    expiration_date = models.DateField()
    verified = models.BooleanField(default=False)


class License(models.Model):
    jumper = models.ForeignKey(
        JumperProfile,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=1,
        choices=(
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        ),
    )
    number = models.PositiveIntegerField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.type + '-' + str(self.number)