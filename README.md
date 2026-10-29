# Seguimiento y caracterización de satélites

**Universidad Nacional de Río Negro (UNRN)**  
**Materia:** Programación I  
**Alumno:** Benjamín Rivas  
**Lenguaje:** Python 3

## Descripción

Este proyecto tiene como objetivo analizar un catálogo de satélites mediante Python, utilizando herramientas de procesamiento de datos, programación orientada a objetos y cálculo de posiciones orbitales.

Se trabaja con un archivo JSON proporcionado por la cátedra, que contiene información de **16.710 satélites** obtenida de CelesTrak.

El programa permite:

- Leer y procesar un catálogo de satélites.
- Clasificar satélites según su grupo y año de lanzamiento.
- Calcular posiciones geográficas utilizando Skyfield.
- Clasificar órbitas según su altitud (LEO, MEO, GEO y HEO).
- Obtener estadísticas de altitudes por grupo.
- Identificar los satélites de mayor y menor altitud.
- Filtrar satélites dentro de una zona geográfica.
- Presentar los resultados mediante Jupyter Notebook.

## Estructura del proyecto

```text
proyesat/
├── datos/
│   └── satelites.json
├── salidas/
├── catalogo.py
├── satelite.py
├── analisis.py
├── funciones_base.py
├── informe.ipynb
├── README.md
└── .gitignore
```

## Descripción de los módulos

### `catalogo.py`

Contiene las funciones encargadas de leer el archivo JSON, identificar grupos de satélites, obtener sus años de lanzamiento y realizar conteos.

### `satelite.py`

Define la clase `Satelite`, que almacena:

- Nombre
- Latitud
- Longitud
- Altitud en kilómetros

También contiene la función `crear_satelites()`, que utiliza Skyfield para calcular las posiciones y crear los objetos correspondientes.

### `analisis.py`

Contiene funciones para:

- Contar satélites por tipo de órbita.
- Buscar los satélites de mayor y menor altitud.
- Ordenar satélites por distintos atributos.
- Filtrar satélites según una zona geográfica.
- Calcular estadísticas de altitud por grupo.

### `funciones_base.py`

Módulo proporcionado por la cátedra que contiene las funciones necesarias para realizar cálculos orbitales utilizando Skyfield.

### `informe.ipynb`

Notebook de Jupyter que integra los módulos desarrollados y presenta los resultados del análisis.

### `datos/satelites.json`

Catálogo de satélites proporcionado por la cátedra.

## Instalación

### Requisitos

- Python 3.14
- NumPy
- Matplotlib
- Skyfield
- JupyterLab

### 1. Crear el entorno virtual

Desde la carpeta raíz del proyecto:

```bash
python3.14 -m venv .venv
```

### 2. Activar el entorno

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
python -m pip install numpy matplotlib skyfield jupyterlab ipykernel
```

## Ejecución

Con el entorno virtual activado, iniciar JupyterLab:

```bash
python -m jupyterlab
```

Abrir el archivo `informe.ipynb` y ejecutar todas las celdas en orden.

También se puede utilizar Visual Studio Code, seleccionando el intérprete de Python correspondiente a `.venv`.

## Desarrollo

El proyecto fue desarrollado individualmente por **Benjamín Rivas**.

Se implementaron los siguientes módulos:

- `catalogo.py`: lectura, clasificación y conteo de registros.
- `satelite.py`: implementación de la clase `Satelite` y creación de objetos.
- `analisis.py`: funciones de análisis y estadísticas.
- `informe.ipynb`: integración de los módulos y presentación de resultados.

Los archivos `funciones_base.py` y `datos/satelites.json` fueron proporcionados por la cátedra.

## Fuente de datos

Los datos utilizados provienen de [CelesTrak](https://celestrak.org/NORAD/elements/) y fueron suministrados por la cátedra.

Las posiciones se calculan para el instante de ejecución del programa.

La precisión de las posiciones puede disminuir a medida que aumenta la diferencia entre el instante calculado y la fecha de referencia de los datos orbitales.