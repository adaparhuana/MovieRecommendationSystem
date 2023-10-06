from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from typing import List
from typing import Union
from typing import Optional
#import uvicorn

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.get("/boton/", response_class=HTMLResponse)
async def boton(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("boton.html", context)

# Leer el archivo CSV con la información de las películas
df = pd.read_csv('df_platforms.csv')

# 1ra funcion : Película con mayor duración
@app.get("/get_max_duration")
def get_max_duration(year: Optional[int] = None, platform: Optional[str] = None, duration_type: Optional[str] = None):
    global df
    df = pd.read_csv("df_platforms.csv")
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."

    # Filtrar según los filtros indicados
    if year:
        df = df[df["release_year"] == year]
    if platform:
        df = df[df["platform"] == platform.lower()]
    if duration_type:
        if duration_type in ["m","mi", "min"]:
            df = df[df["duration_type"] == "min"]
        elif duration_type in ["season", "seasons"]:
            df = df[df["duration_type"] == "season"]
    
    # Verificar si hay datos en el DataFrame después de aplicar los filtros
    if df.empty:
        return "No se encontraron datos con los filtros especificados."
    
    # Encontrar la película o serie con la duración máxima
    max_duration_idx = df["duration_int"].idxmax()
    max_duration_title = df.loc[max_duration_idx].title

    return max_duration_title
  

# 2da funcion : Cantidad de películas por plataforma con un puntaje mayor a XX 
@app.get("/get_score_count")
def get_score_count(platform: str, scored: float, year: int)-> Union[int, str]:
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."
    
    # Filtrar las películas de la plataforma y año especificados
    platform_year_movies = df.query(f"platform == '{platform}' and release_year == {year}")
    
    # Seleccionar las películas con una puntuación mayor a 'scored'
    high_score_movies = platform_year_movies.loc[platform_year_movies['average_score'] > scored]
    
    # Contar el número de películas que cumplen con los criterios anteriores y retornar el valor
    count_movies = high_score_movies['title'].count()

    # Retornor la cantidad de películas
    return count_movies

# 3da funcion : Cantidad de películas por plataforma 
@app.get("/get_count_platform")
def get_count_platform(platform:str)-> Union[int, str]:
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."
    
    # Filtrar las películas de la plataforma especificada
    platform_year_movies = df.query(f"platform == '{platform}'")
    
    # Contar el número de películas que cumple con el criterio anterior
    count_movies = platform_year_movies['platform'].count()

    # Retornor la cantidad de películas
    return count_movies

# 4da funcion : Actor que más se repite según plataforma y año
@app.get("/get_actor")
def get_actor(platform: str, year: int):
    global df
    # Verificar si la plataforma es válida
    valid_platforms = ["amazon", "disney", "hulu", "netflix"]
    if platform not in valid_platforms:
        return "Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas."

    # Filtrar por año y plataforma
    filtered_df = df[(df['platform'] == platform) & (df['release_year'] == year)]

    # Excluir los valores "unknown" en la columna 'cast'
    actors = filtered_df['cast'].str.split(',').explode().str.strip()
    actors = actors[actors != "unknown"]
    
    # Obtener el actor que más se repite en la columna 'cast'    
    actor_count = actors.value_counts()
    if actor_count.empty:
        return None
    else:
        return actor_count.index[0]