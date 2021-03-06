from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Lead(models.Model):

    #Model of the leads (DataBase)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    #Foreign key
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        #String representation of the model
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):

    #Model for the Agent (DataBase)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        #String representation of the model
        return self.user.email
