from django.urls import path
from . import views

urlpatterns=[
    path('', views.index2, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='service'),
    path('contact_us/', views.contact, name='contact'),
    path('pojects/', views.project, name='project'),
    path('logistics/', views.logistics, name='logistics'),
    path('handyman/', views.handyman, name='handyman'),
    path('engine/', views.engine, name='engine'),
path('index2/', views.index2, name='index2'),

]
