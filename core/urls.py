from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('pos/', views.pos_view, name='pos'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('portal/', views.portal_cliente_view, name='portal_cliente'),
]