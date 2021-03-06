import sys

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import User

def user_register_view(request):
    on = False
    of = False
    if request.POST.get('offline', False) == 'on':
        on= True
    else:
        of= True
    print(request)
    if request.POST.get('phone','') == '':
        return render(request, 'index.html')
    phone_number = request.POST.get('phone','')[-9:]
    phone_number = '+998' + phone_number
    phones = User.objects.all().filter(phone_number=phone_number)
    if phones:
        return render(request, 'registeryes.html')


    try:
        user = User.objects.create(
            user_fish=request.POST.get('name', ''),
            phone_number=phone_number,
            offline_auditoriya=on,
            online_zoom=of
        )
        if user:
            return render(request, 'register.html')
    except:
        print(sys.exc_info())
    return render(request, 'index.html')
