from django.shortcuts import render
from  .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def classifications(request):
    matches = Match.objects.all().select_related('home_team', 'away_team')  # Optimize query by selecting related teams

    # Calculate points for each team
    classificacao = {}
    for match in matches:
        home_team, away_team = match.home_team, match.away_team
        if home_team not in classificacao:
            classificacao[home_team] = 0
        if away_team not in classificacao:
            classificacao[away_team] = 0

        # Award points based on win/loss (adjust logic if needed)
        if match.home_team_goals > match.away_team_goals:
            classificacao[home_team] += 3
        elif match.home_team_goals < match.away_team_goals:
            classificacao[away_team] += 3
        else:  # Draw
            classificacao[home_team] += 1
            classificacao[away_team] += 1

    # Combine team and points into a list of tuples
    classificacao = sorted(classificacao.items(), key=lambda x: x[1], reverse=True)

    context = {'classificacao': classificacao}
    return render(request, 'classification.html', context)


def table(request):
    matches = Match.objects.all().select_related('home_team', 'away_team')
    context = {'matches': matches}
    return render(request, 'table.html', context)