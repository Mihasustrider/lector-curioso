# core/views.py
from django.shortcuts import render
from .models import Producto, Cliente

def dashboard_view(request):
    # En un proyecto real, aquí irían los cálculos de KPIs
    context = {
        'total_ventas_hoy': 1250.75,
        'libros_mas_vendidos': ['El Señor de los Anillos', 'Cien Años de Soledad'],
        'stock_bajo_count': 5,
    }
    return render(request, 'core/dashboard.html', context)

def pos_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'core/pos.html', context)

def inventario_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'core/inventario.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'core/clientes.html', context)

def portal_cliente_view(request):
    # Simulación de un cliente logueado
    context = {
        'cliente_nombre': 'Carlos López',
        'historial_compras': Producto.objects.order_by('?')[:3], # 3 productos al azar
        'recomendaciones': Producto.objects.order_by('?')[:3],
    }
    return render(request, 'core/portal_cliente.html', context)