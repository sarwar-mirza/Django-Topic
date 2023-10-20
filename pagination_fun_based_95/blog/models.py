from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_body = models.TextField(max_length=500)
    publish_date = models.DateTimeField()
