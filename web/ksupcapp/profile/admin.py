from django.contrib import admin

from .models import Person
from .models import Phone

admin.site.register(Person)
admin.site.register(Phone)
