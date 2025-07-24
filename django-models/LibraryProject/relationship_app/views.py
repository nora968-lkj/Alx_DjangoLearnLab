from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book, Library, UserProfile

# ✅ عرض كل الكتب (function-based view)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ عرض تفاصيل مكتبة (class-based view)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ✅ تسجيل مستخدم جديد
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ✅ View خاص بالـ Admin فقط
@login_required
def admin_view(request):
    try:
        if request.user.userprofile.role == 'Admin':
            return HttpResponse("✅ Welcome Admin! You have access.")
        else:
            return HttpResponse("❌ Access Denied. Admins only.", status=403)
    except UserProfile.DoesNotExist:
        return HttpResponse("❌ User profile not found.", status=404)
