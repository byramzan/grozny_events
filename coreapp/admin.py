from django.contrib import admin

from coreapp.models import Meeting, Customer, Event
# Register your models here.
admin.site.register(Meeting)
admin.site.register(Customer)
admin.site.register(Event)
admin
