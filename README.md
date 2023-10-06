
<p align="center">
  <img src="src\movie.jpg">
</p>

<!-- TABLA DE CONTENIDO -->
## Indice
<details open="open">
  <summary>Tabla de contenido: </summary>
  <ol>
    <li>
      <a href="#Introducción">Introducción</a>
    </li>
    <li>
      <a href="#Objetivo">Objetivo</a>
    </li>
    <li>
      <a href="#ETL">ETL</a>
    </li>
    <li>
      <a href="#EDA">EDA</a>
    </li>
    <li>
      <a href="#Desarrollo-API">Desarrollo API</a>
    </li>
    <li>
      <a href="#Sistema-de-Recomendación">Sistema de Recomendación</a>
    </li>
    <li>
      <a href="#Stack-tecnológico">Stack tecnológico</a>
    </li>   
  </ol>
</details>


## Introducción
Como parte de la etapa de labs de Data Science en Henry, se nos asignó el rol de MLOps Engineer para crear un modelo de Machine Learning de un Sistema de Recomendación de servicios de plataformas streaming de películas y series.

Para este proyecto, se nos proporcionaron los datasets sin procesar de las plataformas: Amazon Prime Video, Disney Plus, Hulu y Netflix, y como los datos de calificaciones (ratings).

[Datasets (raw)](https://drive.google.com/drive/folders/1r7IV_C0Z_uv5NL0whHwE7E0z-MYkU0ww?usp=sharing)


## Objetivo
Recopilar, analizar y procesar los datos con el fin de desarrollar un sistema de recomendación  utilizando algoritmos de Machine Learning para proporcionar a los usuarios recomendaciones personalizadas de películas.

## ETL
El proceso de ETL involucró el tratamiento de los datos contenidos en cuatro archivos CSV de plataformas y ocho archivos CSV de calificaciones (ratings).

Los querimientos de este proceso de tratamiento incluyeron:

+ Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

+ Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”).

+ De haber fechas, deberán tener el formato AAAA-mm-dd

+ Los campos de texto deberán estar en minúsculas, sin excepciones

+ El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).

## EDA
EL proceso de EDA consistió en utilizar técnicas y herramientas para analizar y explorar los datos con el objetivo de obtener información útil para la realizar nuestro modelo de ML de Sistema de Recomendación.

DICCIONARIO DE DATOS

|Features | Descripción|
| --- | --- | 
|id | Identificación de la plataforma con la película|
|show_id | Identificación de la película|
|title | Título de la película|
|director | Director de la película|
|cast | Actores de reparto|
|country | País de la procedencia de la Película|
|date_added | Fecha de agregada a la plataforma|
|release_year | Año de lanzamiento|
|rating | calificación|
|duration | Duración de la película|
|listed_in | Lista de tipo de película|
|description | Descripción de la película|
|plataforma | Tìpo de plataforma|
|duration_int | Duración de la película (entero)|
|duration_type | Tipo de duración de la película|

## Desarrollo API
Para el desarrollo de la API se utilizó el framework FastAPI. Para lo cual se dispuso de los datos ya tratados en el proceso de ETL.

Se realizaron 4 funciones en python para la realizar las consultas asignadas. Siendo estas las siguientes:

1. Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration (year, platform, duration_type)).

2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count (platform, scored, year)).

3. Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform (platform)).

4. Actor que más se repite según plataforma y año. (La función debe llamarse get_actor (platform, year)).

[Ir a la API](https://xxxx)
 
## Sistema de Recomendación
El desarrollo del Sistema de Recomendación consistió en sugerir películas o series a usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. Con este proposito se seleccionó el algoritmo de SVD (Singular Value Decomposition) para entrenar el modelo.

[Ir al sistema de recomendación de películas ](https://huggingface.co/spaces/adaap/Streaming)



## Stack tecnológico
+ Python
+ FastAPI
+ Render
+ Hugging Face






