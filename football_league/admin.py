from django.contrib import admin
from  .models import *

class EventInline(admin.TabularInline):  # Use TabularInline for tabular view
    model = Event
    fields = ["match", "event_type", "player", "time"]
    ordering = ("time",)

class MatchAdmin(admin.ModelAdmin):
    inlines = [EventInline]  # Add EventInline to inlines attribute

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match, MatchAdmin)