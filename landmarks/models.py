from django.db import models
from django.contrib.auth import get_user_model

class Landmark(models.Model):
    title = models.CharField(max_length=100)
    desciption = models.TextField(null=True, blank=True)
    inspiration = models.CharField(max_length=200)
    coordinate_1 = models.FloatField()
    coordinate_2 = models.FloatField()
    preview = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Image(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')