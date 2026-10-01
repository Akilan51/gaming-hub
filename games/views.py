from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import ReviewForm


def home(request):
    games = Game.objects.all().order_by("-created_at")

    return render(
        request,
        "home.html",
        {"games": games}
    )


def games_list(request):
    games = Game.objects.all().order_by("-created_at")

    return render(
        request,
        "games.html",
        {"games": games}
    )


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()

            return redirect("game_detail", game_id=game.id)

    else:
        form = ReviewForm()

    return render(
        request,
        "game_detail.html",
        {
            "game": game,
            "form": form
        }
    )


def buy_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    return render(
        request,
        "buy_game.html",
        {"game": game}
    )