from django.contrib import admin
from  .models import *

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Event)