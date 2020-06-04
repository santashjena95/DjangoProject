from django.shortcuts import render

from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    """
    dest1=Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Odisha'
    dest2.desc = 'The Temple City'
    dest2.img = 'destination_2.jpg'
    dest2.price = 450

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.desc = 'The Modern City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 550

    dest = [dest1, dest2, dest3]
    """
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest})