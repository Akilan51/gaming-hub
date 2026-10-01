from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("games/", views.games_list, name="games_list"),

    path(
        "game/<int:game_id>/",
        views.game_detail,
        name="game_detail"
    ),

    path(
        "game/<int:game_id>/buy/",
        views.buy_game,
        name="buy_game"
    ),
]