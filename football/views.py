from rest_framework import viewsets
from .serializers import LigaSerializer, TeamSerializer, NewGameSerializer, OldGameSerializer
from .models import Liga, Team, NewGame, OldGame

class LigaViewSet(viewsets.ModelViewSet):
    serializer_class = LigaSerializer
    queryset = Liga.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class NewGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewGameSerializer
    queryset = NewGame.objects.all()

class OldGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OldGameSerializer
    queryset = OldGame.objects.all()