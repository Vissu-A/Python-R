from django.contrib import admin

# Register your models here.

from quickstart.models import userdata
# from quickstart.models import mongouserdata

admin.site.register(userdata)
# admin.site.register(mongouserdata)