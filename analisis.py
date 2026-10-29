def contar_por_tipo(satelites):
    """
    Devuelve un diccionario con la cantidad
    de satélites de cada tipo de órbita.
    """
    conteos = {
        "LEO": 0,
        "MEO": 0,
        "GEO": 0,
        "HEO": 0
    }

    for satelite in satelites:
        eltipo = satelite.tipo_orbita(satelite)
        conteos[eltipo] += 1

    return conteos

def mas_bajo(satelites):
    """
    Devuelve el objeto Satelite de menor altitud.
    """
    if not satelites:
        return None

    sat_menor = satelites[0]

    for satelite in satelites:
        if satelite.altitud_km < sat_menor.altitud_km:
            sat_menor = satelite

    return sat_menor

def mas_alto(satelites):
    """
    Devuelve el objeto Satelite de mayor altitud.
    """
    if not satelites:
        return None

    sat_mayor = satelites[0]

    for satelite in satelites:
        if satelite.altitud_km > sat_mayor.altitud_km:
            sat_mayor = satelite

    return sat_mayor
