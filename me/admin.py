from django.contrib import admin
from .models import Persona, Skill, Project

# Register your models here.

class SkillsPersonaInline(admin.TabularInline):
    model = Persona.skills.through

class SkillsProjectInline(admin.TabularInline):
    model = Project.skills.through

class PersonaAdmin(admin.ModelAdmin):
    inlines = [
        SkillsPersonaInline,
    ]
    exclude = ('skills',)



class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        SkillsProjectInline,
    ]
    exclude = ('skills',)

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Skill)

