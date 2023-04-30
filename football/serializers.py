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
    class Meta:
        model = NewGame
        fields = '__all__'


class OldGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldGame
        fields = '__all__'
