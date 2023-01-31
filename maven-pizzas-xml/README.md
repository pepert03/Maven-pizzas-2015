Reporte XML de tipologia y predicción semanal
=================

## Introducción
Instalar librerías de Python necesarias:
```
pip install -r requirements.txt
```
Todos los archivos necesarios se encuentran en la carpeta `data`. Entre ellos se encuentra ```semanas.csv``` obtenido en 
[maven-pizzas-2016](https://github.com/pepert03/maven-pizzas-2016).

## Predicción
Para realizar la predicción se debe ejecutar el script ```predicción.py```. Este script genera un archivo ```predicción.csv``` con la predicción de los ingredientes de cada semana.

## Reporte XML
Para generar el reporte XML se debe ejecutar el script ```pizzas_to_xml.py```, que convierte ```predicción.csv``` en un archivo .json. Luego se genera el reporte XML con el script ```pizzas.xml``` con el reporte de tipología y una predicción de ingredientes por semana.
