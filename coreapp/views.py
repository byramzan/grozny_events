from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from coreapp.forms import AccountForm, UserForm, MeetingForm, EventForm
from coreapp.models import Event

# Create your views here.
def home(request):
    return redirect(meeting_order)

@login_required(login_url='/meeting/sign_in/')
def meeting_home(request):
    return render(request, 'meeting/home.html', {})

def meeting_sign_up(request):
    user_form = UserForm()
    meeting_form = MeetingForm()

    if request.method == "POST":
     user_form = UserForm(request.POST)
     meeting_form = MeetingForm(request.POST, request.FILES)
     
     if user_form.is_valid() and meeting_form.is_valid():
        new_user = User.objects.create_user(**user_form.cleaned_data)
        new_meeting = meeting_form.save(commit=False)
        new_meeting.user = new_user
        new_meeting.save()

        login(request, authenticate(
           username = user_form.cleaned_data["username"],
           password = user_form.cleaned_data["password"]
        ))
        return redirect(meeting_home)
    


    return render(request, 'meeting/sign_up.html', {
        "user_form": user_form,
        "meeting_form": meeting_form
    })
@login_required(login_url='/meeting/sign_in/')
def meeting_account(request):

   if request.method == "POST":
      account_form = AccountForm(request.POST, instance=request.user)
      meeting_form = MeetingForm(request.POST, instance=request.user.meeting)

      if account_form.is_valid() and meeting_form.is_valid():
         account_form.save() 
         meeting_form.save()
   account_form = AccountForm(instance=request.user)
   meeting_form = MeetingForm(instance=request.user.meeting)
   
   return render(request, 'meeting/account.html', {
      "account_form": account_form,
      "meeting_form": meeting_form
   })



@login_required(login_url='/meeting/sign_in/')
def meeting_report(request):
   return render(request, 'meeting/report.html', {})

@login_required(login_url='/meeting/sign_in/')
def meeting_order(request):
   return render(request, 'meeting/order.html', {})

@login_required(login_url='/meeting/sign_in/')
def meeting_events(request):
   events = Event.objects.filter(meeting=request.user.meeting).order_by("id")
   return render(request, 'meeting/events.html', {
      "events":events
   })

@login_required(login_url='/meeting/sign_in/')
def meeting_add_events(request):

   if request.method == "POST":
      event_form = EventForm(request.POST)

      if event_form.is_valid():
         event = event_form.save(commit=False)
         event.meeting = request.user.meeting
         event.save()
         return redirect(meeting_events)

   event_form = EventForm()
   return render(request, 'meeting/add_events.html', {
      "event_form": event_form
   })

@login_required(login_url='/meeting/sign_in/')
def meeting_edit_events(request, event_id):

   if request.method == "POST":
      event_form = EventForm(request.POST, instance=Meal.objects.get(id=meal))

      if event_form.is_valid():
         event_form.save()
         return redirect(meeting_event)

   event_form = EventForm(instance=Event.objects.get(id=event_id))
   return render(request, 'meeting/edit_event.html', {
      "event_form": event_form
   })

