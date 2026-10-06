# Przykłady zapytań Django ORM

1. **filter**: `Game.objects.filter(price__gt=100)`
2. **exclude**: `Game.objects.exclude(category__name='party')`
3. **get**: `Game.objects.get(id=1)`
4. **count**: `Game.objects.filter(players_count__gte=4).count()`
5. **order_by**: `Game.objects.all().order_by('-price')`
6. **lookup z __**: `Game.objects.filter(title__icontains='Catan')`
7. **Przejście przez relację (wprost)**: `Game.objects.first().category.name`
8. **Przejście przez relację (odwrotnie)**: `Category.objects.get(id=1).games.all()`