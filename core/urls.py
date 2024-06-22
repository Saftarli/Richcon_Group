from django.urls import path
from .views import index, about, contact, projects, blogs

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='project'),
    path('blogs', blogs, name='blogs'),

]
