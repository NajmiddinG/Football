from rest_framework import viewsets
from .serializers import LigaSerializer, TeamSerializer, NewGameSerializer, OldGameSerializer
from .models import Liga, Team, NewGame, OldGame

class LigaViewSet(viewsets.ModelViewSet):
    serializer_class = LigaSerializer
    queryset = Liga.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        queryset = queryset.order_by('-ochko', '-nisbat', 'tur')
        return queryset

class NewGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewGameSerializer

    def get_queryset(self):
        queryset = NewGame.objects.all()
        return queryset.order_by('-date')

class OldGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OldGameSerializer

    def get_queryset(self):
        queryset = OldGame.objects.all()
        return queryset.order_by('-date')