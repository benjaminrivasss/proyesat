class Satelite:
    def __init__(self,nombre, latitud, longitud, altitud_km):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

    def tipo_orbita(self):
        """
        Devuelve LEO, MEO, GEO o HEO
        según la altitud del satélite.
        """
        altitud = self.altitud_km

        if altitud < 2000:
            return "LEO"
        elif altitud < 34000:
            return "MEO"
        elif altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def esta_en_zona(self, zona):
        """
        Devuelve True si el satélite se encuentra
        dentro de los límites de la zona.
        """
        lon_min, lat_min, lon_max, lat_max = zona
        if lon_min <= self.longitud <= lon_max:
            if lat_min <= self.latitud <= lat_max:
                return True
        return False

    def __str__(self):
        """Devuelve una representacion de texto del satelite"""
        return f'{self.nombre} ,|,{self.tipo_orbita()},|,{self.altitud_km}'