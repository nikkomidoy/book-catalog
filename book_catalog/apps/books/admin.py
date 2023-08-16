from django.contrib import admin

from book_catalog.apps.books.models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for Book
    """
    list_display = ['title', 'display_categories']
    filter_horizontal = ['categories']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category
    """
    search_fields = ['name']
