from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
#    balance =
#    credit_limit =
#    phone_number =
#    email = 
    birthdate = models.DateField()
