from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.title