from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Gallery,Chef,Waiter,HeroSlide
import random

rand=random.random()*10

# Create your views here.
def index(request):
    gallery=list(Gallery.objects.all()[:5])
    random.shuffle(gallery)

    chefs=list(Chef.objects.all())
    waiters=list(Waiter.objects.all())
    chefs_and_waiters=chefs+waiters #adding the waiters and chefs to present them as staff

    hero_section_slides=HeroSlide.objects.all()

    context={
        "staff":chefs_and_waiters,
        "gallery":gallery,
        "slides":hero_section_slides
    }
    return render(request,"index.html",context)

