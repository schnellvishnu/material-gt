from django.db import models

# Create your models here.
class Data_tbl(models.Model):
    
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    
    
    def __str__(self):
        return (self.name)
        