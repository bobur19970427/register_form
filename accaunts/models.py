from django.db import models

# Create your models here.

class User(models.Model):
    user_fish = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    online_auditoriya = models.BooleanField()
    offline_zoom = models.BooleanField()
    def __str__(self):
        return str(self.user_fish)
