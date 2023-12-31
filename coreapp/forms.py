from django import forms
from django.contrib.auth.models import User
from coreapp.models import Meeting, Event

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ("name", "phone", "address", "time", "logo")

class AccountForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("meeting",)