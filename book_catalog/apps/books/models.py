from django.db import models

from book_catalog.apps.authors.models import Author
from book_catalog.apps.books.utils import get_cover_image_upload_path, valid_jpeg_or_png


class Category(models.Model):
    """
    Model for Category
    """
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Summary of the book")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class Book(models.Model):
    """
    Model for Book
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Summary of the book")
    categories = models.ManyToManyField(Category, help_text="Category of the book")
    cover_image = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_cover_image_upload_path,
        help_text="Book cover image in png/jpg file",
        validators=[valid_jpeg_or_png]
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def cover_image_url(self):
        """
        Get book cover image url
        """
        if not self.cover_image:
            return "https://i.imgur.com/NAZWTGP.png"

        return self.cover_image.url

    def display_categories(self):
        """
        Display list of categories in Admin
        """
        return ', '.join([genre.name for genre in self.categories.all()])

    display_categories.short_description = 'Categories'
