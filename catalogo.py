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
    for i in GRUPOS:
        if nombre.startswith(i):
            return GRUPOS[i]

    return "Grupo fuera de rango"  
