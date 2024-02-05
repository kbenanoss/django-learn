from django.contrib import admin
from .models import Home

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_image', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(Home, HomeAdmin)
