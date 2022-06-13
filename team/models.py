from django.db import models

from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=221)

    def __str__(self):
        return self.position


class Team(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='team')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    about = models.TextField()

    def __str__(self):
        return self.name
