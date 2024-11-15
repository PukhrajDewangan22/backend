from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    item = models.TextField()

    def __str__(self):
        return self.name
   
