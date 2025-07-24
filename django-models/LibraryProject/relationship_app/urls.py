from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ✅ روابط الـ Authentication
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ روابط التطبيق
    path('admin-view/', views.admin_view, name='admin_view'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ للراحة لو فيه حاجة إضافية
    path('dashboard/', views.list_books, name='dashboard'),
]

