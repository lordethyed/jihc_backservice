from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published_date')
    list_filter = ('title', 'published_date')
    search_fields = ('title', 'published_date')


admin.site.register(Article, ArticleAdmin)