from django.db import models
from django.core.validators import RegexValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Assuming one author per book for simplicity
    isbn = models.CharField('ISBN',
                            max_length=13,
                            unique=True,
                            validators=[
                                RegexValidator(
                                    regex='^[0-9Xx\-]+$',
                                    message='ISBN must contain only numbers, or X/x for the 10th character.',
                                    code='invalid_isbn'
                                ),
                            ],
                            )
    is_free = models.BooleanField(default=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.CharField(max_length=100, blank=True)
    pages = models.IntegerField(help_text='Number of pages in the book')
    image_url = models.URLField(max_length=255, blank=True, help_text='URL to the book cover image')
    summary = models.TextField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, help_text='The date and time this record was created.')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Remove hyphens from isbn before saving
        self.isbn = self.isbn.replace('-', '')
        super(Book, self).save(*args, **kwargs)

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'