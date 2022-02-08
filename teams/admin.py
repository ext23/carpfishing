from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['name', 'id', 'external_code', ]


admin.site.register(Team, TeamAdmin)
