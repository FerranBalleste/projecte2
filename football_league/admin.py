from django.contrib import admin
from  .models import *

class EventInline(admin.TabularInline):  # Use TabularInline for tabular view
    model = Event
    fields = ["match", "event_type", "player", "time"]
    ordering = ("time",)

class MatchAdmin(admin.ModelAdmin):
    inlines = [EventInline]  # Add EventInline to inlines attribute
    readonly_fields = ["home_team_goals", "away_team_goals"]
    search_fields = ["home_team","away_team"]

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match, MatchAdmin)