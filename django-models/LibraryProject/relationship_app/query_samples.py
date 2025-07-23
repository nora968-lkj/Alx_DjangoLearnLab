from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def list_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print("📚 كل الكتب لمؤلف محدد:")
    for book in books:
        print(f"- {book.title}")

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print("🏛️ كل الكتب في مكتبة محددة:")
    for book in books:
        print(f"- {book.title}")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print("👩‍💼 أمين المكتبة لمكتبة محددة:")
    print(f"Librarian: {librarian.name}")

# Call the functions for testing
list_books_by_author("Naguib Mahfouz")
list_books_in_library("Central Library")
get_librarian_for_library("Central Library")
