from django.db import models


class Paste(models.Model):
    text = models.TextField()
    url = models.CharField(max_length=10)