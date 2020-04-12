from django.contrib import admin
#from .models import UserProfile
from profiles_api import models

# Register your models here.
# admin.site.register(UserProfile)
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
