from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Meeting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='meeting')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    time = models.DateTimeField(null=True, blank=True)
    logo = CloudinaryField('image')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models. CharField (max_length=255)
    phone = models. CharField (max_length=255, blank=True)
    address = models. CharField (max_length=255, blank=True)
    
    def __str__(self):
        return self.name
        
class Event(models.Model): 
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='meetings')
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=500)
def __str__(self):
    return self.name