from django.db import models

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    collcover=models.CharField(max_length=100)

    def __str__(self):
        return self.name