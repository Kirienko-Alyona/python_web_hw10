from django.db import models

# Create your models here.

class Author(models.Model):

    fullname = models.CharField(unique=True, max_length=100, null=False)
    born_date = models.CharField(unique=False, max_length=30, null=False)
    born_location = models.CharField(unique=False, max_length=150, null=False)
    description = models.TextField(unique=True, null=False)
    
    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):

    tags = models.CharField(unique=False, max_length=100, null=True)
    author = models.ForeignKey(Author, to_field="id", on_delete=models.CASCADE, unique=False)
    quote = models.TextField(unique=True, null=False)
    
    # def __str__(self):
    #     return f"{self.name}"