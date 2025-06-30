from django.urls import path
from . import views

urlpatterns=[
    path('', views.index2, name='index'),
    path('about/', views.about, name='about'),

    path('contact_us/', views.contact, name='contact'),
    path('pojects/', views.project, name='project'),
    path('logistics/', views.logistics, name='logistics'),
    path('handyman/', views.handyman, name='handyman'),
    path('engine/', views.engine, name='engine'),
    path('enginepics/', views.enginepics, name='enginepics'),
    path('handymanpics/', views.handymanpics, name='handymanpics'),
    path('logisticpics/', views.logisticpics, name='logisticpics'),

    # Detail views for sitemap and get_absolute_url
    path('engine/<int:pk>/', views.engine_detail, name='engine_detail'),
    path('logistics/<int:pk>/', views.logistic_detail, name='logistic_detail'),
    path('handyman/<int:pk>/', views.handyman_detail, name='handyman_detail'),


]
