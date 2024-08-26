from django.contrib import admin
from .models import Gallery,Chef,Waiter,HeroSlide

# Register your models here.
interface_models=[Gallery,HeroSlide]
other=[Chef,Waiter]

admin.site.register(interface_models)

admin.site.register(other)


