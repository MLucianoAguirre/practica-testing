def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad


def aplicar_descuento(monto, porcentaje):
    return monto - (monto * porcentaje / 100)

def calcular_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["precio"] * item["cantidad"]
    return subtotal