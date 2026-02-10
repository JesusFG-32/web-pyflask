# Conference Schedule App

Una aplicación web simple construida con Flask para mostrar y buscar en una agenda de conferencias.

## Características

- **Ver Agenda**: Muestra una lista completa de las charlas y eventos programados.
- **Búsqueda**: Funcionalidad de búsqueda para encontrar eventos por título, categoría o nombre del ponente.
- **Detalle de Ponentes**: Información sobre los ponentes vinculada a cada charla.

## Requisitos

- Python 3.x
- Flask

## Instalación

1.  Clona este repositorio o descarga los archivos.
2.  (Opcional) Crea y activa un entorno virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows use: .venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1.  Ejecuta la aplicación:
    ```bash
    python app.py
    ```
    O usando el script incluido (si estás en Linux/Mac):
    ```bash
    ./run_dev.sh
    ```

2.  Abre tu navegador y ve a:
    `http://127.0.0.1:5000`

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask. Contiene los datos de ejemplo y las rutas.
- `templates/`: Contiene las plantillas HTML (index.html, base.html).
- `static/`: Archivo estáticos como CSS y JavaScript.
- `requirements.txt`: Lista de dependencias del proyecto.
