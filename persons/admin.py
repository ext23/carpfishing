from django.contrib import admin
from .models import Person, Member, Judge

admin.site.register(Person)
admin.site.register(Member)
admin.site.register(Judge)
