from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'isbn', 'image_url', 'created_date')
    list_filter = ('author', 'genre', 'is_free','created_date')
    search_fields = ('title', 'isbn', 'author__first_name', 'author__last_name')
    raw_id_fields = ('author',)
    date_hierarchy = 'created_date'
    ordering = ('title', 'created_date')
    filter_horizontal = ('genre',)
    readonly_fields = ('created_date',)
    actions = ['make_free', 'make_not_free']

    def make_free(self, request, queryset):
        queryset.update(is_free=True)

    make_free.short_description = "Mark selected books as free"

    def make_not_free(self, request, queryset):
        queryset.update(is_free=False)

    make_not_free.short_description = "Mark selected books as not free"
