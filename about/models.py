from django.db import models

# Create your models here.

class About(models.Model):
    about_text = models.TextField(max_length=200)
    image = models.ImageField(upload_to="images")
