from django.db import models


class Snippet(models.Model):
    snippet_name = models.CharField(max_length=20)
    snippet_privacy = models.BooleanField(default=False)
    snippet_expiry = models.CharField(max_length=3)
    snippet_file = models.CharField(max_length=1000)
