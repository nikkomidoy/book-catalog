from django.urls import path

from .views import BookDetailView, BookListView, BooksByCategoryListView, IndexTemplateView

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("categories/<int:id>/books/", BooksByCategoryListView.as_view(), name="book-by-category-list"),
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="books-detail"),
]
