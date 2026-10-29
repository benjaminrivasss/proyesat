from catalogo import grupo
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
        eltipo = satelite.tipo_orbita()
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

def en_zona(satelites, zona):
    """devuelve una lista de los satélites dentro de la zona """
    dentro_de_zona = []
    for satelite in satelites:
        checkeo = satelite.esta_en_zona(zona)
        if checkeo == True:
            dentro_de_zona.append(satelite)
    return dentro_de_zona

def ordenar_por(satelites, atributo, descendente=False):
    """
    Devuelve una lista nueva de satélites
    ordenada según el atributo indicado.
    """
    return sorted(
        satelites,
        key=lambda sat: getattr(sat, atributo),
        reverse=descendente
    )

def top_n(satelites, n, mas_altos=True):
    """devuelve los n satélites más altos o mas bajos"""
    if mas_altos:
        lista_altos = ordenar_por(satelites,'altitud_km',True)
        return lista_altos[:n]
    
    lista_bajos = ordenar_por(satelites,'altitud_km',False)
    return lista_bajos[:n]

def resumen_por_grupo(satelites):
    """
    Devuelve un resumen de las altitudes
    de los satélites de cada grupo.
    """
    altitudes_por_grupo = {}

    for satelite in satelites:
        nombre_grupo = grupo(satelite.nombre)
        altitud = satelite.altitud_km

        if nombre_grupo in altitudes_por_grupo:
            altitudes_por_grupo[nombre_grupo].append(altitud)
        else:
            altitudes_por_grupo[nombre_grupo] = [altitud]
    resumen = {}
    for nombre_grupo, altitudes in altitudes_por_grupo.items():
        cantidad = len(altitudes)
        minima = min(altitudes)
        media = sum(altitudes) / cantidad
        maxima = max(altitudes)

        resumen[nombre_grupo]= {
            'cantidad':cantidad,
            'minima':minima,
            'media':media,
            'maxima':maxima
        }

    return resumen
        
