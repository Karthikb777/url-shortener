from django.db import models


# Create your models here.
class url(models.Model):
    full_url = models.URLField()
    ext = models.TextField(max_length=10)


# CREATE TABLE url(INTEGER id PRIMARYKEY, VARCHAR full_url, VARCHAR ext)
# SELECT * FROM url