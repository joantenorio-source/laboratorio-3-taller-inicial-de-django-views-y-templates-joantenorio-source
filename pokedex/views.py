from django.shortcuts import render

# Página principal
def index(request):
    pokemons = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Gengar"]
    return render(request, 'index.html', {'pokemons': pokemons})


# Página de detalles
def pokemon_details(request, pokemon):
    frases = {
        "Pikachu": "¡Pika Pika! La electricidad siempre está de mi lado.",
        "Charizard": "Mis llamas arden con fuerza en cada batalla.",
        "Bulbasaur": "La naturaleza me da poder y energía.",
        "Squirtle": "¡Nada como una buena batalla acuática!",
        "Gengar": "Las sombras son mi hogar favorito."
    }

    frase = frases.get(
        pokemon,
        f"¡Hola! Soy {pokemon} y estoy listo para combatir."
    )

    context = {
        'pokemon': pokemon,
        'frase': frase
    }

    return render(request, 'details.html', context)