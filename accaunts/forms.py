from django import forms
from .models import *
class details_forms(forms.ModelForm):
    user_fish = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    phone_number = forms.CharField(required=True,max_length=50)
    online_auditoriya = forms.BooleanField()
    offline_zoom = forms.BooleanField()
    class Meta():
        model = User
        fields = ['user_fish','phone_number','online_auditoriya','offline_zoom']