from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_fish', 'phone_number', 'offline_auditoriya', 'online_zoom')

admin.site.unregister(Group)
admin.site.site_header = 'islom-moliyasi uz | admin'