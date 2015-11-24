from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='index'),
    url(r'^blogs/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog'),
    url(r'^categories.html$', views.CategorieListView.as_view(), name='categories'),
    url(r'^categories/(\d+)/$', views.CategorieBlogListView.as_view(), name='categories-detail'),
    url(r'^projects.html$', views.ProjectListView.as_view(), name='projects'),
    url(r'^aboutme.html$', views.AboutmeListView.as_view(), name='aboutme'),
]
