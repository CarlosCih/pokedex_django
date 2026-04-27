from django.shortcuts import render
from django.views import View
from .services import PokemonService

# Create your views here.

class HomeView(View):
    """Vista para la página de inicio."""
    
    template_name = 'core/home.html'
    
    def get(self, request):
        """Maneja las solicitudes GET para la página de inicio."""
        return render(request, self.template_name)
    
    def detalle_pokemon(self, request, pokemon_id):
        """Maneja las solicitudes para mostrar el detalle de un Pokémon."""
        pokemon_service = PokemonService()
        pokemon = pokemon_service.get_pokemon_by_id(pokemon_id)
        return render(request, 'core/pokemon_detail.html', {'pokemon': pokemon})
