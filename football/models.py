from django.db import models


class Liga(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Liga/')

    def __str__(self):
        return "Liga -> " + self.name


class Team(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Liga/')
    tur = models.IntegerField(default=0)
    nisbat = models.IntegerField(default=0)
    ochko = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.liga}: Jamoa -> " + self.name


class NewGame(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='new_games_player1')
    player2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='new_games_player2')
    date = models.DateTimeField()

    def __str__(self):
        return f"Yangi o'yin -> {self.player1.name} vs {self.player2.name}"


class OldGame(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='old_games_player1')
    player2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='old_games_player2')
    natija = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Eski o'yin -> {self.player1.name} {self.natija} {self.player2.name}"