from django.db import models
# Create your models here.


class SampleData(models.Model):
    url = models.CharField(max_length=100)
    data = models.TextField()
