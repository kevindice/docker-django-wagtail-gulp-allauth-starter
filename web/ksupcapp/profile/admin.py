from django.contrib import admin

from .models import Person
from .models import Phone
from .models import JumperProfile
from .models import Rating

admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(JumperProfile)
admin.site.register(Rating)