from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('service',views.services,name='service'),
]

