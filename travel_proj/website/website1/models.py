from django.db import models

# Create your models here.
class tour(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descrip=models.TextField()

    def __str__(self):
        return self.name
class people(models.Model):
    names = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc= models.TextField()

    def __str__(self):
        return self.names