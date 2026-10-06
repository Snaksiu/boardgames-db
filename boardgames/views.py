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
    
from django.db.models import Avg, Min, Max, Count

def stats(request):
    # Agregacja na poziomie bazy danych bez pętli w Pythonie
    price_stats = Game.objects.aggregate(
        avg_price=Avg('price'),
        min_price=Min('price'),
        max_price=Max('price')
    )
    
    # Liczba rekordów w każdej kategorii
    category_stats = list(Category.objects.annotate(
        games_count=Count('games')
    ).values('name', 'games_count'))

    data = {
        "total_records": Game.objects.count(),
        "categories_summary": category_stats,
        "avg_price": round(price_stats['avg_price'] or 0, 2),
        "min_price": float(price_stats['min_price'] or 0),
        "max_price": float(price_stats['max_price'] or 0)
    }
    return JsonResponse(data)

from django.db import connection

def health_check(request):
    try:
        connection.ensure_connection()
        return JsonResponse({"status": "ok", "database": "connected"})
    except Exception:
        return JsonResponse({"status": "error", "database": "disconnected"}, status=503)

def info(request):
    categories = list(Category.objects.values_list('name', flat=True))
    return JsonResponse({
        "database_engine": connection.vendor,
        "total_games": Game.objects.count(),
        "available_categories": categories
    })