from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('clients/', views.show_clients, name='clientes'),
    path('clients/delete/<int:client_id>/', views.delete, name='delete'),
    path('clients/editar/<int:client_id>/', views.editar, name='editar'),
]
