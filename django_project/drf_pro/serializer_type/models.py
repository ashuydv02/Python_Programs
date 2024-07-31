from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Score(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()
    
    def __str__(self):
        return self.player_name
