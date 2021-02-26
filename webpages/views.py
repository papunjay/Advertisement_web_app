from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders=Slider.objects.all()
    teams = Team.objects.all()
    features=Youtuber.objects.order_by('name').filter(is_featured=True)
    data={
        'sliders':sliders,
        'teams':teams,
        'features':features,
    }
    return render(request,'webpages/home.html',data)

def about(request):
     return render(request,"webpages/about.html")

def services(request):
     return render(request,"webpages/services.html")

def contac(request):
     return render(request,"webpages/contac.html")

