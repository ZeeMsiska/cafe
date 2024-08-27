from typing import Any
from django.db import models
from time import time
from datetime import datetime

# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=50)
    event_price=models.CharField(max_length=15)
    event_description=models.CharField(max_length=1024, blank=True)
    event_img=models.ImageField(default='img.png')

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
    description=models.CharField(max_length=2000,  blank=True)
    bg=models.ImageField()

class About(models.Model):
    description=models.CharField(max_length=1024, blank=True)

class Special(models.Model):
    title=models.CharField(max_length=250)
    food_name=models.CharField(max_length=255)
    description=models.CharField(max_length=1024, blank=True)
    pic=models.ImageField(default='img.png')

class Contact(models.Model):
    location=models.CharField(max_length=1024)
    opening_hours=models.TimeField()
    email=models.EmailField(max_length=254)
    phone=models.IntegerField(max_length=13)

    def __str__(self):
        return f"Location: {self.location}, opening_hours:{self.opening_hours.strftime('%H')}, email:{self.email}"

class Comment(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=1024)

class Book(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=1024)
    num_pple = models.IntegerField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def booking_summary(self):
        """Returns a summary of the booking details."""
        return (f"Booking for {self.name} ({self.email})\n"
                f"Phone: {self.phone}, Number of People: {self.num_pple}\n"
                f"Date: {self.date.strftime('%Y-%m-%d')}, Time: {self.time.strftime('%H:%M:%S')}\n"
                f"Message: {self.message}")

    def __str__(self):
        return f"Booking: {self.name} on {self.date.strftime('%Y-%m-%d')} at {self.time.strftime('%H:%M:%S')}"

