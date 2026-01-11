from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    blogs = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
