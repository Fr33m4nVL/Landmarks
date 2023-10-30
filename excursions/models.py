from django.db import models

class Excursion(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    number = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title