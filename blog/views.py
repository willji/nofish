from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog, Categorie, Project, Aboutme

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'

class CategorieListView(ListView):
    model = Categorie
    template_name = 'blog/categories.html'

class CategorieBlogListView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, pk=self.args[0])
        return Blog.objects.filter(categorie=self.categorie)

class ProjectListView(ListView):
    model = Project
    template_name = 'blog/projects.html'

class AboutmeListView(ListView):
    model = Aboutme
    template_name = 'blog/aboutme.html'
