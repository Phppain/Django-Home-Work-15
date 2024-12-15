from django.db import models

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=256)

    def __str__(self):
        return self.author
