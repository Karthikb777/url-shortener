from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_url = models.URLField()
    ext = models.TextField(max_length=10)

