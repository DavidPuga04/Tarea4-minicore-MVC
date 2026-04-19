from django.urls import path
from .views import *

urlpatterns = [
    path('ventas/', listar_ventas),
    path('ventas/crear/', crear_venta),
    path('ventas/eliminar/<int:id>/', eliminar_venta),
    path('comisiones/', calcular_comisiones),
    path('vendedores/', listar_vendedores),
]