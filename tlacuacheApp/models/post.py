from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="images", null=True)
    description = models.TextField()