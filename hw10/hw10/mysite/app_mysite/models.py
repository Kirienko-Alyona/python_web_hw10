from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):

    fullname = models.CharField(unique=True, max_length=100, null=False)
    born_date = models.DateField(unique=False, null=False)
    born_location = models.CharField(unique=False, max_length=500, null=False)
    description = models.TextField(unique=True, max_length=2700, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):

    quote = models.TextField(unique=True, null=False)
    author = models.ForeignKey(Author, to_field="id", on_delete=models.CASCADE, unique=False)
    tags = ArrayField(models.CharField(max_length=50), null=False, blank=True, unique=False)
    
    def __str__(self):
        return f"{self.tags}"