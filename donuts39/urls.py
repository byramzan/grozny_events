"""donuts39 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from coreapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('meeting/sign_in/', auth_views.LoginView.as_view(template_name='meeting/sign_in.html'), name='meeting_sign_in'),
    path('meeting/sign_out/', auth_views.LogoutView.as_view(next_page='/'), name='meeting_sign_out'),
    path('meeting/sign_up/', views.meeting_sign_up, name='meeting_sign_up'),
    path('meeting/', views.meeting_home, name='meeting_home'),

    path('meeting/account/', views.meeting_account, name='meeting_account'),
    path ('meeting/order/', views. meeting_order, name='meeting_order'), 
    path ('meeting/report/', views.meeting_report, name='meeting_report'),
    path ('meeting/events/', views.meeting_events, name='meeting_events'),
    path('meeting/events/add/', views.meeting_add_events, name='add_meeting_events'),
    path('meeting/events/edit/<int:event_id>', views.meeting_edit_events, name='edit_meeting_events'),



]
