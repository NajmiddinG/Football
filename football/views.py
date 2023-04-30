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
        liga_id = self.request.query_params.get('liga_id', None)
        if liga_id is None:
            liga_id = Liga.objects.first().id
        
        if liga_id is not None:
            queryset = queryset.filter(liga_id=liga_id)
        queryset = queryset.order_by('-ochko', '-nisbat', 'tur')
        return queryset

class NewGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewGameSerializer

    def get_queryset(self):
        liga_id = self.request.query_params.get('liga')
        if liga_id:
            queryset = NewGame.objects.filter(liga=liga_id)
        else:
            first_liga = Liga.objects.first()
            queryset = NewGame.objects.filter(liga=first_liga.id)

        return queryset.order_by('-date')

class OldGameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OldGameSerializer

    def get_queryset(self):
        liga_id = self.request.query_params.get('liga')
        if liga_id:
            queryset = OldGame.objects.filter(liga=liga_id)
        else:
            first_liga = Liga.objects.first()
            queryset = OldGame.objects.filter(liga=first_liga.id)
        return queryset.order_by('-date')