from django.contrib import admin
from .models import *

# Register your models here.

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['logo']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['ProjectName', 'Description']

admin.site.register(SkillsModel, SkillsAdmin)
admin.site.register(Projects, ProjectsAdmin)