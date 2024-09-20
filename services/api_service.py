import requests

api_key = 'cc0bbbd7774ce2853272ceeb3db7db56'
base_url_api = 'https://api.themoviedb.org/3'

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

def pagina_peliculas():
    endpoints = [
        f'{base_url_api}/movie/popular?api_key={api_key}&language=es-ES&page=1',
        f'{base_url_api}/movie/upcoming?api_key={api_key}&language=es-ES&page=1',
        f'{base_url_api}/movie/top_rated?api_key={api_key}&language=es-ES&page=1',
        f'{base_url_api}/movie/now_playing?api_key={api_key}&language=es-ES&page=1',
    ]
    peliculas_con_posters = []
    base_url_poster = 'https://image.tmdb.org/t/p/w500'
    ids_ya_agregados = set()

    for url in endpoints:
        # Repetir por varias páginas
        for page in range(1, 4):  # Ajusta el rango según sea necesario
            response = requests.get(url.replace('page=1', f'page={page}'))  # Cambia la página en la URL
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

def obtener_series_proximas():
    url = f'{base_url_api}/tv/on_the_air?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        series = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        series_con_posters = [
            {
                'id': serie['id'],
                'title': serie['name'],  # Para series, el campo es 'name'
                'poster_url': base_url + serie['poster_path']
            }
            for serie in series if serie['poster_path']
        ]
        return series_con_posters
    return []

def obtener_series_populares():
    url = f'{base_url_api}/tv/popular?api_key={api_key}&language=es-ES&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        series = data['results']
        base_url = 'https://image.tmdb.org/t/p/w500'
        series_con_posters = [
            {
                'id': serie['id'],
                'title': serie['name'],  # Para series, el campo es 'name'
                'poster_url': base_url + serie['poster_path']
            }
            for serie in series if serie['poster_path']
        ]
        return series_con_posters
    return []

def obtener_detalles_pelicuas(movie_id):
    url = f'{base_url_api}/movie/{movie_id}?api_key={api_key}&language=es-ES'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None