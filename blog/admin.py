from django.contrib import admin
from .models import Blog, Categorie, Project, Aboutme

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'modified_time']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Categorie)
admin.site.register(Project)
admin.site.register(Aboutme)

