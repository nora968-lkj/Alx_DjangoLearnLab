# Django Admin Configuration for Book Model

We configured the Django admin interface to manage the `Book` model from the `bookshelf` app.

## Steps

1. Registered the `Book` model in `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)