from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.TextField()#link
    description = models.TextField()
    url = models.TextField()#link