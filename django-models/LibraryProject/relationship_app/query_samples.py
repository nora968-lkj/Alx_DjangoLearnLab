import os
import django

# إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ✅ إضافة بيانات للتجربة
# إنشاء مؤلف
author1 = Author.objects.create(name="Naguib Mahfouz")
author2 = Author.objects.create(name="Taha Hussein")

# إنشاء كتب
book1 = Book.objects.create(title="The Cairo Trilogy", author=author1)
book2 = Book.objects.create(title="Children of Gebelawi", author=author1)
book3 = Book.objects.create(title="The Days", author=author2)

# إنشاء مكتبة
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

# إضافة كتب للمكتبات
library1.books.add(book1, book2)
library2.books.add(book2, book3)

# إنشاء أمين مكتبة
librarian1 = Librarian.objects.create(name="Sara Ahmed", library=library1)
librarian2 = Librarian.objects.create(name="Mohamed Ali", library=library2)

# ✅ استعلامات
print("\n📚 كل الكتب لمؤلف محدد:")
books_by_author = Book.objects.filter(author__name="Naguib Mahfouz")
for book in books_by_author:
    print(f"- {book.title}")

print("\n🏛️ كل الكتب في مكتبة محددة:")
library_books = Library.objects.get(name="Central Library").books.all()
for book in library_books:
    print(f"- {book.title}")

print("\n👩‍💼 أمين المكتبة لمكتبة محددة:")
librarian = Librarian.objects.get(library__name="Community Library")
print(f"Librarian: {librarian.name}")
