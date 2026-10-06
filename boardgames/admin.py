from django.contrib import admin
from .models import Category, Game

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'release_date', 'players_count')
    list_filter = ('category', 'release_date')
    search_fields = ('title', 'description')