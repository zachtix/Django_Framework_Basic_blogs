from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    def __str__(self):
        post_name = self.name
        return post_name
    