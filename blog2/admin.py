from django.contrib import admin

# Register your models here.
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'views', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    readonly_fielsds = ('views',)



admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
