from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    fb = models.CharField(max_length=100, blank=True, null=True)
    x = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.title  

