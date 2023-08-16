from typing import Any

from django.views.generic import DetailView, ListView, TemplateView

from book_catalog.apps.books.models import Book, Category


class IndexTemplateView(TemplateView):
    """
    Index template view for home page
    """
    template_name = "base.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context.update({
            'categories': categories
        })
        return context


class BooksByCategoryListView(TemplateView):
    """
    Template view for Books by category
    """
    template_name = "books/books_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(id=kwargs.get('id'))
        books = category.book_set.all()
        context.update({
            "books": books,
            "category": category,
        })
        return context


class BookListView(ListView):
    """
    List of books and search books view
    """
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "all_search_results"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_query = self.request.GET.get('query', "")
        context.update({
            "last_query": last_query,
        })
        return context

    def get_queryset(self):
       queryset = super().get_queryset()
       query = self.request.GET.get('query')

       if query:
          postresult = Book.objects.filter(title__icontains=query)
          queryset = postresult

       return queryset


class BookDetailView(DetailView):
    """
    Detail view for Book
    """
    model = Book
