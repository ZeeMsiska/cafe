from django.db import models

# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=50)
    event_price=models.CharField(max_length=15)

class Menu(models.Model):
    menu_name=models.CharField(max_length=100)
    menu_price=models.CharField(max_length=15)
    menu_description=models.CharField(max_length=255)
    
class Gallery(models.Model):
    pic=models.ImageField()
    description=models.CharField(max_length=255, blank=True)#optional

class Waiter(models.Model):
    pic=models.ImageField()
    first_name=models.CharField(max_length=55)
    last_name=models.CharField(max_length=55)
    position=models.CharField(max_length=60, default="waiter")

    def __str__(self):
        return self.first_name+" "+self.last_name

class Chef(models.Model):
    pic=models.ImageField()
    first_name=models.CharField(max_length=55)
    last_name=models.CharField(max_length=55)
    position=models.CharField(max_length=60, default="chef")

    def __str__(self):
        return self.first_name+" "+self.last_name
    

class HeroSlide(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=2000)
    bg=models.ImageField()