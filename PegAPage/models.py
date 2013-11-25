from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    Board_name = models.CharField(max_length=200,unique=True)
    user = models.ForeignKey(User)
    Board_des =  models.CharField(max_length=64)    

           
class Peg(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.URLField(unique=True)
    image = models.CharField(max_length=64)
    peg_des =  models.CharField(max_length=64)
    #Like_desc = models.CharField(max_length=64)
    boards = models.ManyToManyField(Board)
    
class Comments(models.Model):
    comments_desc = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    peg = models.ForeignKey(Peg)
    
class Follow(models.Model):
    user = models.ForeignKey(User)
    board = models.ForeignKey(Board)