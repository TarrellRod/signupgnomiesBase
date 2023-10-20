from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    event_category = models.CharField(max_length=100)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def get_absolute_url(self):
        return reverse('events-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.event_name
    
class Category(models.Model):
    event = models.ForeignKey(Event, related_name="categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number_of_slots = models.IntegerField()

    def get_absolute_url(self):
        return reverse('categories-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return '%s - %s' % (self.event.event_name, self.name)
    

class Slot(models.Model):
    category = models.ForeignKey(Category, related_name="slots", on_delete=models.CASCADE)
    slot_holder_firstname = models.CharField(max_length=52)#,name='firstname')
    slot_holder_lastname = models.CharField(max_length=52)
    slot_holder_email = models.EmailField(max_length=255,default='gnomie@example.com')
    slot_holder_student = models.CharField(max_length=52,default='gnome')

    def __str__(self):
        return '%s - %s' % (self.category.name, (self.slot_holder_firstname +' ' + self.slot_holder_lastname))