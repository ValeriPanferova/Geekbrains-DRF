from django.contrib import admin

from .models import TODO, Project

admin.site.register(Project)
admin.site.register(TODO)
