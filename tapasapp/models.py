from django.db import models


# Create your models here.

class Dish(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    objects = models.Manager()

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=300)
    Password = models.CharField(max_length=30)
    objects = models.Manager()

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password


def __str__(self):
    return str(self.pk) + ": " + self.name

def __str__(self):
    return self.Username


