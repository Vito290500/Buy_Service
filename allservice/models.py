from django.db import models

# Create your models here.
class User_Profile(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)    
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


