import json

GRUPOS = {
    "STARLINK": "Starlink",
    "ONEWEB": "OneWeb",
    "KUIPER": "Kuiper",
    "QIANFAN": "Qianfan",
    "IRIDIUM": "Iridium",
    "GLOBALSTAR": "Globalstar",
    "NAVSTAR": "GPS",
    "BEIDOU": "BeiDou"
}

def leer_satelites(ruta):
    """
    Lee el catálogo de satélites desde un archivo JSON.
    Devuelve una lista de registros.
    """
    
    try: 
        with open(ruta,encoding='utf-8') as archivo:
            registros = json.load(archivo)

        return registros
            
    except FileNotFoundError:
        print(f'("Error: No se encontró el archivo {ruta}"')
        return []
        
def anio_lanzamiento(registro):
    """
    Devuelve el año de lanzamiento de un satélite
    a partir de su identificador internacional.
    """
    identificador = registro["OBJECT_ID"]
    anio = int(identificador[:4])

    return anio


def grupo(nombre):
    """Devuelve el grupo al que pertenece un satélite."""
    for i in GRUPOS:
        if nombre.startswith(i):
            return GRUPOS[i]

    return "Otros"  

def contar_por_grupo(registros):
    """
    Recibe una lista de registros y devuelve
    un diccionario con la cantidad de satélites
    de cada grupo.
    """
    conteos = {}

    for registro in registros:
        name = registro["OBJECT_NAME"]
        empresa = grupo(name)
        if empresa in conteos:
            conteos[empresa] += 1
        else:
            conteos[empresa] = 1

    return conteos

def lanzamientos_por_anio(registros):
    """
    Devuelve un diccionario con la cantidad de
    satélites lanzados en cada año.
    """
    conteos = {}

    for registro in registros:
       anio = anio_lanzamiento(registro)
       if anio in conteos:
            conteos[anio] += 1
       else:
            conteos[anio] = 1
       
    return conteos