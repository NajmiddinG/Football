from django.contrib import admin
from .models import Liga, Team, NewGame, OldGame


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['liga', 'name','tur','nisbat','ochko']

@admin.register(NewGame)
class NewGameAdmin(admin.ModelAdmin):
    list_display = ['liga','player1','player2','date']

@admin.register(OldGame)
class OldGameAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):   
        NewGame.objects.filter(liga=obj.liga,player1=obj.player1,player2=obj.player2).delete()

        obj.player1.tur += 1
        obj.player2.tur += 1
        a, b = map(int, obj.natija.split(':'))
        obj.player1.nisbat += a-b
        obj.player2.nisbat += b-a
        if a>b:
            obj.player1.ochko += 3
        elif b>a:
            obj.player2.ochko += 3
        else:
            obj.player1.ochko += 1
            obj.player2.ochko += 1

        obj.player1.save()
        obj.player2.save()

        super().save_model(request, obj, form, change)