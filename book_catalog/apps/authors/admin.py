from django.contrib import admin

from book_catalog.apps.authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for Author
    """
    search_fields = ['first_name', 'last_name']
