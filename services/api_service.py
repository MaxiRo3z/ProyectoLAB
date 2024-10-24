import requests

api_key = 'cc0bbbd7774ce2853272ceeb3db7db56'
base_url_api = 'https://api.themoviedb.org/3'


CATEGORIAS = {
    'populares': 'popular',
    'proximas': 'upcoming',
    'en_cartelera': 'now_playing',
    'mejor_puntuadas': 'top_rated'
}

CATEGORIAS_SERIES= {
    'populares': 'popular',
    'se_emiten_hoy': 'airing_today',
    'en_television': 'on_the_air',
    'mejor_puntuadas': 'top_rated'
}

def obtener_peliculas_proximas():
    url = f'{base_url_api}/movie/upcoming?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        peliculas = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        peliculas_con_posters = [
            {
                'id': pelicula['id'],
                'title': pelicula['title'],
                'poster_url': base_url + pelicula['poster_path']
            }
            for pelicula in peliculas if pelicula['poster_path']
        ]
        return peliculas_con_posters
    return []

def obtener_peliculas():
    endpoints = [
        f'{base_url_api}/movie/popular?api_key={api_key}&language=es-ES&page=1',
    ]
    peliculas_con_posters = []
    base_url_poster = 'https://image.tmdb.org/t/p/w500'
    ids_ya_agregados = set()

    for url in endpoints:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            peliculas = data['results']
            for pelicula in peliculas:
                ruta_poster = pelicula['poster_path']
                movie_id = pelicula['id']
                if ruta_poster and movie_id not in ids_ya_agregados:
                    url_completa_poster = base_url_poster + ruta_poster
                    peliculas_con_posters.append({
                        'id': movie_id,
                        'titulo': pelicula['title'],
                        'url_poster': url_completa_poster
                    })
                    ids_ya_agregados.add(movie_id)
    return peliculas_con_posters



def pagina_peliculas(categoria, page=1):
    if categoria in CATEGORIAS:
        endpoint = CATEGORIAS[categoria]
        url = f'{base_url_api}/movie/{endpoint}?api_key={api_key}&language=es-ES&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            peliculas = data['results']
            base_url = 'https://image.tmdb.org/t/p/w500'
            peliculas_con_posters = [
                {
                    'id': pelicula['id'],
                    'title': pelicula['title'],
                    'poster_url': base_url + pelicula['poster_path']
                }
                for pelicula in peliculas if pelicula['poster_path']
            ]
            total_pages = min(data['total_pages'], 500)  # Limitar total_pages a un máximo de 500
            return peliculas_con_posters, total_pages
    return [], 1

def pagina_series(categoria, page=1):
    if categoria in CATEGORIAS_SERIES:
        endpoint = CATEGORIAS_SERIES[categoria]
        url = f'{base_url_api}/tv/{endpoint}?api_key={api_key}&language=es-ES&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            series = data['results']
            base_url = 'https://image.tmdb.org/t/p/w500'
            series_con_posters = [
                {
                    'id': serie['id'],
                    'name': serie['name'],  # Cambia 'title' por 'name'
                    'poster_url': base_url + serie['poster_path']
                }
                for serie in series if serie.get('poster_path')  # Usa get para evitar errores
            ]
            total_pages = min(data['total_pages'], 500)  # Limitar total_pages a un máximo de 500
            return series_con_posters, total_pages
    return [], 1

def obtener_series_proximas():
    url = f'{base_url_api}/tv/on_the_air?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        series = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        series_con_posterso = [
            {
                'id': serie['id'],
                'title': serie['name'],  # Para series, el campo es 'name'
                'poster_url': base_url + serie['poster_path']
            }
            for serie in series if serie['poster_path']
        ]
        return series_con_posterso
    return []

def obtener_series_populares():
    url = f'{base_url_api}/tv/top_rated?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        series = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        series_con_postersp = [
            {
                'id': serie['id'],
                'title': serie['name'],  # Para series, el campo es 'name'
                'poster_url': base_url + serie['poster_path']
            }
            for serie in series if serie['poster_path']
        ]
        return series_con_postersp
    return []

def obtener_detalles_pelicuas(movie_id):
    base_url_poster = 'https://image.tmdb.org/t/p/w500'
    base_url_backdrop = 'https://image.tmdb.org/t/p/original'
    response = requests.get(f"{base_url_api}/movie/{movie_id}?api_key={api_key}&language=es-ES")
    credits_response = requests.get(f"{base_url_api}/movie/{movie_id}/credits?api_key={api_key}&language=es-ES")
    videos_response = requests.get(f"{base_url_api}/movie/{movie_id}/videos?api_key={api_key}&language=es-ES")

    if response.status_code == 200 and credits_response.status_code == 200 and videos_response.status_code == 200:
        data = response.json()
        credits_data = credits_response.json()
        video_response = requests.get(f"{base_url_api}/movie/{movie_id}/videos?api_key={api_key}&language=es-ES")

    if response.status_code == 200 and credits_response.status_code == 200 and video_response.status_code == 200:
        data = response.json()
        credits_data = credits_response.json()
        video_response = requests.get(f"{base_url_api}/movie/{movie_id}/videos?api_key={api_key}&language=es-ES")

    if response.status_code == 200 and credits_response.status_code == 200 and video_response.status_code == 200:
        data = response.json()
        credits_data = credits_response.json()
        video_data = video_response.json()

        # Filtrar el equipo (crew) para obtener director y guionista
        crew = credits_data['crew']
        directores = [person['name'] for person in crew if person['job'] == 'Director']
        guionistas = [person['name'] for person in crew if person['job'] in ['Screenplay', 'Writer']]

        # Obtener el primer tráiler de YouTube disponible
        trailer_url = None
        for video in video_data['results']:
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                trailer_url = f"https://www.youtube.com/embed/{video['key']}"
                break

        detalles_pelicula = {
            'titulo_pelicula': data['title'],
            'anio_estreno': data['release_date'][:4],
            'clasificacion': 'PG-13' if data['adult'] else 'PG',
            'fecha_estreno': data['release_date'],
            'generos': ', '.join([g['name'] for g in data['genres']]),
            'duracion': f"{data['runtime']} mins",
            'puntuacion_usuario': int(data['vote_average'] * 10),
            'resumen_pelicula': data['overview'],
            'director': ','.join(directores) if directores else 'Desconocido',
            'guionista': ','.join(guionistas) if guionistas else 'Desconocido',
            'url_poster': base_url_poster + data['poster_path'],
            'url_backdrop': base_url_backdrop + data['backdrop_path'] if data['backdrop_path'] else None,
            'trailer_url': trailer_url  # Añadimos la URL del tráiler
        }
        return detalles_pelicula
    
def obtener_detalles_series(serie_id):
    base_url_poster = 'https://image.tmdb.org/t/p/w500'
    base_url_backdrop = 'https://image.tmdb.org/t/p/original'

    response = requests.get(f"{base_url_api}/tv/{serie_id}?api_key={api_key}&language=es-ES")
    credits_response = requests.get(f"{base_url_api}/tv/{serie_id}/credits?api_key={api_key}&language=es-ES")
    
    if response.status_code == 200 and credits_response.status_code == 200:
        data = response.json()
        credits_data = credits_response.json()

        # Filtrar el equipo (crew) para obtener director y guionista
        crew = credits_data['crew']
        directores = [person['name'] for person in crew if person['job'] == 'Director']
        guionistas = [person['name'] for person in crew if person['job'] in ['Screenplay', 'Writer']]

        detalles_serie = {
            'titulo_pelicula': data['name'],
            'anio_estreno': data['first_air_date'][:4],
            'clasificacion': 'PG-13' if data['adult'] else 'PG',
            'fecha_estreno': data['first_air_date'],
            'generos': ', '.join([g['name'] for g in data['genres']]),
            'duracion': f"{data['episode_run_time'][0]} mins" if data['episode_run_time'] else 'Desconocido',
            'puntuacion_usuario': int(data['vote_average'] * 10),
            'resumen_pelicula': data['overview'],
            'director': ','.join(directores) if directores else 'Desconocido',  # Añadir lógica para obtener el director
            'guionista': ','.join(guionistas) if guionistas else 'Desconocido',  # Añadir lógica para obtener el guionista
            'url_poster': base_url_poster + data['poster_path'],
            'url_backdrop': base_url_backdrop + data['backdrop_path'] if data['backdrop_path'] else None  # Imagen de fondo
        }
    return detalles_serie

def pagina_actores(page=1):
    """Obtiene los actores populares de la API de TMDB."""
    url = f'{base_url_api}/person/popular?api_key={api_key}&language=es&page={page}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        actores = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        
        actores_con_fotos = [
            {
                'id': actor['id'],
                'name': actor['name'],
                'profile_url': base_url + actor['profile_path'] if actor.get('profile_path') else None,
            }
            for actor in actores if actor.get('profile_path')  # Solo actores con imagen
        ]
        
        total_pages = min(data['total_pages'], 500)  # Limitar a 500 para evitar problemas de paginación
        return actores_con_fotos, total_pages
    
    return [], 1

