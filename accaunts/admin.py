from django.contrib import admin

# Register your models here.
from . import models
from .models import User
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_fish', 'phone_number', 'online_auditoriya', 'offline_zoom')

