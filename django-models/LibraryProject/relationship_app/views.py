from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView

# 📚 عرض كل الكتب
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 🏛️ عرض تفاصيل مكتبة
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# 👤 تسجيل مستخدم جديد
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# 🔐 تسجيل دخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# 🚪 تسجيل خروج
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ✅ Admin View (بشكل صارم)
@login_required
def admin_view(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'Admin':
        return render(request, 'relationship_app/admin_dashboard.html')
    else:
        return render(request, 'relationship_app/not_allowed.html')




