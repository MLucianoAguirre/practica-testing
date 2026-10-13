from calculos import calcular_total, aplicar_descuento, calcular_subtotal


def test_calcular_total_multiplica_precio_por_cantidad():
    resultado = calcular_total(1500, 3)
    assert resultado == 4500


def test_aplicar_descuento_con_porcentaje_comun():
    resultado = aplicar_descuento(1000, 10)
    assert resultado == 900


def test_aplicar_descuento_con_cero_porciento_devuelve_mismo_monto():
    resultado = aplicar_descuento(1500, 0)
    assert resultado == 1500


def test_aplicar_descuento_del_cien_porciento_devuelve_cero():
    resultado = aplicar_descuento(800, 100)
    assert resultado == 0

def test_calcular_subtotal_con_multiples_items():
    items = [
        {"precio": 1500, "cantidad": 2},  # 1500 * 2 = 3000
        {"precio": 800, "cantidad": 3}    # 800 * 3 = 2400
    ]
    # El subtotal real debería ser 3000 + 2400 = 5400
    assert calcular_subtotal(items) == 5400