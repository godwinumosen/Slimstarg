
from django.urls import path
from . import views

app_name = 'slimstarg'

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('events/', views.events, name='events'),
    path('tophit/', views.tophit, name='tophit'),
    path('contact/',views.contact, name='contact'),
    path('ack/', views.admin, name='ack')
    
]
