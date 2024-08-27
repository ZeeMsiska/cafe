from django.contrib import admin
from .models import Gallery,Chef,Waiter,HeroSlide,Special,Events,About,Contact,Comment,Book

# Register your models here.
interface_models=[Gallery,HeroSlide,Special,Events]
other=[Chef,Waiter,Contact,Comment,Book]

admin.site.register(interface_models)

admin.site.register(other)


