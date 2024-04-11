from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField()
    steps = models.CharField()

    def __str__(self):
        return self.title