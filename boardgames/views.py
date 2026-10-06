from django.http import JsonResponse
from .models import Game, Category

def list_games(request):
    games = Game.objects.all()
    
    # Filtrowanie
    category_id = request.GET.get('category')
    if category_id:
        games = games.filter(category_id=category_id)
        
    data = [
        {
            "id": g.id,
            "title": g.title,
            "category": g.category.name,
            "price": float(g.price),
            "release_date": str(g.release_date),
            "players_count": g.players_count
        } for g in games
    ]
    return JsonResponse(data, safe=False)

def game_detail(request, id):
    try:
        g = Game.objects.get(id=id)
        return JsonResponse({
            "id": g.id,
            "title": g.title,
            "category": g.category.name,
            "price": float(g.price),
            "release_date": str(g.release_date),
            "players_count": g.players_count
        })
    except Game.DoesNotExist:
        return JsonResponse({"error": f"Game with id {id} not found."}, status=404)