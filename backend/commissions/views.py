from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Venta, Regla, Vendedor


# Crud 
@api_view(['GET'])
def listar_ventas(request):
    ventas = Venta.objects.all()
    data = []

    for v in ventas:
        data.append({
            "id": v.id,
            "vendedor": v.vendedor.nombre,
            "monto": v.monto,
            "fecha": v.fecha
        })

    return Response(data)


@api_view(['POST'])
def crear_venta(request):
    vendedor_id = request.data.get('vendedor')
    monto = request.data.get('monto')
    fecha = request.data.get('fecha')

    venta = Venta.objects.create(
        vendedor_id=vendedor_id,
        monto=float(monto),
        fecha=fecha
    )

    return Response({"mensaje": "Venta creada"})


@api_view(['DELETE'])
def eliminar_venta(request, id):
    try:
        venta = Venta.objects.get(id=id)
        venta.delete()
        return Response({"mensaje": "Venta eliminada"})
    except Venta.DoesNotExist:
        return Response({"error": "Venta no encontrada"}, status=404)


# Vendedores

@api_view(['GET'])
def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    data = []

    for v in vendedores:
        data.append({
            "id": v.id,
            "nombre": v.nombre
        })

    return Response(data)


# Comisiones

def calcular_comision(monto):
    reglas = Regla.objects.all().order_by('-monto_minimo')

    for regla in reglas:
        if monto >= regla.monto_minimo:
            return monto * (regla.porcentaje / 100)

    return 0


@api_view(['GET'])
def calcular_comisiones(request):
    inicio = request.GET.get('inicio')
    fin = request.GET.get('fin')

    if not inicio or not fin:
        return Response({"error": "Fechas inválidas"}, status=400)

    ventas = Venta.objects.filter(fecha__range=[inicio, fin])

    resumen = {}
    total_global = 0

    for v in ventas:
        comision = calcular_comision(v.monto)
        nombre = v.vendedor.nombre

        if nombre not in resumen:
            resumen[nombre] = {
                "ventas": 0,
                "comisiones": 0
            }

        resumen[nombre]["ventas"] += v.monto
        resumen[nombre]["comisiones"] += comision
        total_global += comision

    return Response({
        "resumen": resumen,
        "total_comisiones": total_global
    })


# datos de prueba

@api_view(['GET'])
def seed_data(request):
    if Vendedor.objects.exists() or Regla.objects.exists():
        return Response({"mensaje": "Los datos ya existen"})

    # Vendedores
    Vendedor.objects.create(nombre="Juan")
    Vendedor.objects.create(nombre="Maria")
    Vendedor.objects.create(nombre="Carlos")
    Vendedor.objects.create(nombre="Ana")

    # Reglas de comisión
    Regla.objects.create(monto_minimo=0, porcentaje=5)
    Regla.objects.create(monto_minimo=500, porcentaje=10)
    Regla.objects.create(monto_minimo=1000, porcentaje=15)

    return Response({"mensaje": "Datos creados correctamente"})