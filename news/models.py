from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=256)
    image_url = models.URLField(max_length=255, blank=True, help_text='URL to the book cover image')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title