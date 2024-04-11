from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=255, blank=True)
    steps = models.TextField()

    def __str__(self):
        return self.title
    
class Tests(models.Model):
    tests = models.ManyToManyField(Test)