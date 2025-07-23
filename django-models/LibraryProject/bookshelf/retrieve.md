```markdown
```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Example Output:
# 1984 George Orwell 1949

# Retrieve a single book by title
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Example Output:
# 1984 George Orwell 1949