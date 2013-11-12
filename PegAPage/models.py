from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UrlLink(models.Model):
    url = models.URLField(unique=True)

class Bookmark(models.Model):
    bookmarkname = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(UrlLink)

           
class Peg(models.Model):
    name = models.CharField(max_length=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)