from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    about_text = models.TextField()
    about_image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
