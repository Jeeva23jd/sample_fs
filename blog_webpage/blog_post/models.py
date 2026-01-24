from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blogcover = models.ImageField(upload_to='blog_covers/')

    def __str__(self):
        return self.title