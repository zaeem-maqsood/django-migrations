from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    fiction = models.BooleanField(default=True)

    def __str__(self):
        return self.title
