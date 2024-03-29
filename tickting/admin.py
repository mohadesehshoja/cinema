from django.contrib import admin
from tickting.models import Showtime,Cinema,Movie,Ticket
# Register your models here.
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Showtime)
admin.site.register(Ticket)
