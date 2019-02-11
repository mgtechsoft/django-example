from django.db import models

# Create your models here.
class Topic(models.Model):
    top = models.CharField(max_length=242,unique=True)
    
    def __str__(self):
        return (self.top)


class web(models.Model):
    t = models.ForeignKey('Topic',on_delete=models.CASCADE,)
    name = models.CharField(max_length=121,unique=True)


    def __str__(self):
        return (self.name)
    

class Record(models.Model):
    name = models.ForeignKey('web', on_delete=models.CASCADE,)
    date = models.DateField()
     
    def __str__(self):
        return str(self.date)