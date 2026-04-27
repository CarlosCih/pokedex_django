import requests

BASE_URL = 'https://pokeapi.co/api/v2/'
TIMEOUT = 10

def _request(endpoint):
    """Centraliza las solicitudes a la API de PokeAPI."""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud a {url}: {e}")
        return None
    
def get_pokemon_list(limit=20, offset=0):
    """ Obtiene una lista de Pokémon."""
    data = _request(f'pokemon?limit={limit}&offset={offset}')
    if not data:
        return []
    
    pokemons = []
    
    for pokemon in data.get('results', []):
        detalle = get_details(pokemon['name'])
        if detalle:
            pokemons.append(detalle)
    
    return pokemons

def get_details(name):
    """ Obtiene los detalles de un Pokémon por su nombre."""
    data = _request(f'pokemon/{name.lower()}')
    if not data:
        return None
    return {
        "id": data.get("id"),
        "nombre": data.get("name"),
        "imagen": data.get("sprites", {})
            .get("other", {})
            .get("official-artwork", {})
            .get("front_default"),
        "altura": data.get("height"),
        "peso": data.get("weight"),
        "tipos": [
            t["type"]["name"] for t in data.get("types", [])
        ],
        "habilidades": [
            h["ability"]["name"] for h in data.get("abilities", [])
        ],
    }
    
def get_pokemon_by_id(pokemon_id):
    """ Obtiene los detalles de un Pokémon por su ID."""
    data = _request(f'pokemon/{pokemon_id}')
    if not data:
        return None
    return {
        "id": data.get("id"),
        "nombre": data.get("name"),
        "imagen": data.get("sprites", {})
            .get("other", {})
            .get("official-artwork", {})
            .get("front_default"),
        "altura": data.get("height"),
        "peso": data.get("weight"),
        "tipos": [
            t["type"]["name"] for t in data.get("types", [])
        ],
        "habilidades": [
            h["ability"]["name"] for h in data.get("abilities", [])
        ],
    }
    
def search_pokemon(query):
    """ Busca un Pokémon por su nombre o ID."""
    if query.isdigit():
        return get_pokemon_by_id(query)
    else:
        return get_details(query)