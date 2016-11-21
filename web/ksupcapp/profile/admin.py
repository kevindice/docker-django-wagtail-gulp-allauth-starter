from django.contrib import admin

from .models import Profile
from .models import Phone

admin.site.register(Profile)
admin.site.register(Phone)
