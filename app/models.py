from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    year = models.IntegerField()
    box = models.IntegerField()
    
    def __str__(self):
        return f'Title: {self.title}, Director: {self.director}, Year: {self.year}, gender: {self.gender}, box: {self.box}'