import os
import django

# إعداد بيئة Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 📚 كل الكتب لمؤلف معين
author_name = "Naguib Mahfouz"  # 📝 غيّري الاسم لو حبيتي
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"📚 كل الكتب لمؤلف {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"❌ لا يوجد مؤلف باسم {author_name}")

print("\n" + "="*40 + "\n")

# 🏛️ كل الكتب في مكتبة معينة
library_name = "Central Library"  # 📝 غيّري الاسم لو حبيتي
try:
    library = Library.objects.get(name=library_name)
    books_in_library = Book.objects.filter(library=library)
    print(f"🏛️ كل الكتب في مكتبة {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"❌ لا توجد مكتبة باسم {library_name}")

print("\n" + "="*40 + "\n")

# 👩‍💼 أمين المكتبة لمكتبة معينة
try:
    librarian = Librarian.objects.get(library=library)
    print(f"👩‍💼 أمين مكتبة {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"❌ لا يوجد أمين مكتبة لمكتبة {library_name}")
