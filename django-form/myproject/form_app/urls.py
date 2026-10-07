from django.urls import path
from form_app import views

urlpatterns = [
      path('', views.homeView, name='home'),
      path('contact/', views.contactView, name='contact'),
      path('success/', views.successview, name='success'),
]
