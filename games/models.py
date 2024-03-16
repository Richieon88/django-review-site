from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title