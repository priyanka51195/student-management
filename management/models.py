from django.db import models

# Create your models here.
class Entry(models.Model):
    ID =models.CharField(max_length=1000 , primary_key=True)
    name = models.CharField(max_length= 20 )
    address = models.CharField(max_length=50)
    number = models.IntegerField(max_length=10 )
    password = models.CharField(max_length= 15)

    def __str__(self):
        return self.ID


