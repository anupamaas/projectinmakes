from django.db import models
def __str__(self):
    return self.name

class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

# Create your models here.

