from django.db import models

# Create your models here.
#Model for Slider
STATUS = (('active','Active'),('','Default'))
class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')#upload Image code
    text = models.TextField(blank = True)
    rank = models.IntegerField()
    status = models.CharField(choices= STATUS,blank=True,max_length=100)

    def __str__ (self):
        return self.name
