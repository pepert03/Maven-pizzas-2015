Predicción Maven Pizzas 2015
=================

## Introducción
Instalar librerías de Python para el análisis de datos:
```
pip install -r requirements.txt
```
Todos los datos se encuentran en la carpeta `data`, pero si se desea, se puede descargar desde [Kaggle](https://www.kaggle.com/datasets/neethimohan/maven-pizza-challenge-dataset) y despues descomprimir en la carpeta `data`.

## Ejecución
**Nota**: El tiempo de ejecución de `etl.py` es de 3 minutos aprox., los datasets obtenidos ya están guardados en la carpeta `data`, no hace falta ejecutar `etl.py`para hacer la predicción.

Para analizar los datos, se puede ejecutar el script `etl.py`, generando los archivos:
* `data/dias_pizzas.csv`: Contiene la cantidad de pizzas vendidas por día.
* `data/dias.csv`: Contiene la cantidad ingredientes vendidos por día.
* `data/semana.csv`: Contiene la cantidad de ingredientes vendidos por semana.

## Predicción
Para predecir los ingredientes necesarios para una semana, se puede ejecutar el script `predict.py`, e introducir la semana a predecir. Ejemplo:
```
Semana (0-52): 1
```
Generando un diccionario con los ingredientes necesarios para la semana.
