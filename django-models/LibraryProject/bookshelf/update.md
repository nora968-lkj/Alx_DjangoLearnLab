```markdown
```python
from bookshelf.models import Book

# Retrieve the book you want to update
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(pk=book.pk)
print(updated_book.title, updated_book.author, updated_book.publication_year)
# Example Output:
# Nineteen Eighty-Four George Orwell 1949