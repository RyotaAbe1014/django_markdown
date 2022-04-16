from django.contrib import admin

# Register your models here.
from .models import Article, Technologies
 
admin.site.register(Article)
admin.site.register(Technologies)