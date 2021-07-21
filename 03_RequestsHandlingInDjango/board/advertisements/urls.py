from django.urls import path
from . import views

urlpatterns = [
    path('advertisements/', views.Advertisements.as_view()),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('', views.General.as_view()),
]
