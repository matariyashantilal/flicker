from django.contrib import admin
from .models import Location, UserFavouriteList, AddPresetLocation,User

admin.site.register(User)
admin.site.register(Location)
admin.site.register(UserFavouriteList)
admin.site.register(AddPresetLocation)
