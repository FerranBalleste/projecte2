from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import League, Team

def get_leagues(request):
    leagues = League.objects.all()
    leagues_data = []
    for l in leagues:
        leagues_data.append({'id': l.id, 'name': l.name,})
    return JsonResponse(leagues_data, safe=False)

def get_teams(request, league_id):
    try:
        league = League.objects.get(pk=league_id)
        teams = Team.objects.filter(league=league)
        teams_data = []
        for team in teams:
            teams_data.append({'id': team.id, 'name': team.name,})
        return JsonResponse(teams_data, safe=False)
    except League.DoesNotExist:
        return HttpResponse(status=404)
