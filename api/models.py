from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    new_image = models.ImageField(upload_to = 'images/')

