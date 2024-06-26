from django.db import models

class League(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.team})"

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_matches")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_matches")
    date = models.DateField()
    home_team_goals = models.IntegerField(default=0)
    away_team_goals = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.date}) {self.home_team_goals} : {self.away_team_goals}"

class Event(models.Model):
    MATCH_EVENT_CHOICES = (
        ("GOAL", "Goal"),
        ("PENALTY", "Penalty"),
        ("RED_CARD", "Red Card"),
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=MATCH_EVENT_CHOICES)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)  # Optional player for events like goals
    time = models.IntegerField(help_text="Minute of the match the event happened")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.event_type == 'GOAL':  # Update goals only for GOAL events
            match = self.match
            match.home_team_goals = Event.objects.filter(match=match, event_type='GOAL', player__team=match.home_team).count()
            match.away_team_goals = Event.objects.filter(match=match, event_type='GOAL', player__team=match.away_team).count()
            match.save()

    def __str__(self):
        return f"{self.event_type} - {self.match}: {self.player} ({self.time})"
