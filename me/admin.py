from django.contrib import admin
from .models import Persona, Skill, Project, Article

# Register your models here.

class SkillsPersonaInline(admin.TabularInline):
    model = Persona.skills.through

class SkillsProjectInline(admin.TabularInline):
    model = Project.skills.through

class AboutPersonaInline(admin.StackedInline):
    model = Article.owner.through
    # exclude = ('shor_article',)
    extra = 1

class PersonaAdmin(admin.ModelAdmin):
    exclude = ('skills',)
    inlines = [
        SkillsPersonaInline,
        AboutPersonaInline,
    ]
    



class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        SkillsProjectInline,
    ]
    exclude = ('skills',)

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Skill)

