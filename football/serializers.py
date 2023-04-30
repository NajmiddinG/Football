from rest_framework import serializers
from .models import Liga, Team, NewGame, OldGame

class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    liga_name = serializers.ReadOnlyField(source='liga.name')

    class Meta:
        model = Team
        fields = '__all__'


class NewGameSerializer(serializers.ModelSerializer):
    player1 = TeamSerializer()
    player2 = TeamSerializer()
    liga = LigaSerializer()
    class Meta:
        model = NewGame
        fields = ('id','liga','player1','player2', 'date')


class OldGameSerializer(serializers.ModelSerializer):
    player1 = TeamSerializer()
    player2 = TeamSerializer()
    liga = LigaSerializer()
    class Meta:
        model = OldGame
        fields = ('id','liga','player1','player2', 'natija', 'date')
