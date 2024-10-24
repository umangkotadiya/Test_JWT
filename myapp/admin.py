from django.contrib import admin
from .models import User, Hospital, Appointment

admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(Appointment)
