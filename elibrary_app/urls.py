from django.urls import path
from . import views
from .views import deleteBook

from .views import verify_email, send_verification_email
from .views import delete_profile

from django.contrib.auth import views as auth_views


urlpatterns = [
 path('', views.verify_email, name='verify_email'), 
 path("pink", views.pong), # new
  path('explore', views.explore, name='explore'),
  path('home', views.home, name='home'),
  path('register', views.Registers, name='register'),
  path('login', views.Login, name='login'), 
  
  
  path('addBook/<int:user_id>', views.addBook, name='addBook'),
  path('addBook', views.addBook, name='addBook'),
  path('contri/<int:user_id>', views.contri, name='contri'),
  path('logout', views.Login, name='logout'),
  path('deleteBook/<int:book_id>', views.deleteBook, name='deleteBook'),
  path('editBook/<int:book_id>', views.editBook, name='editBook'),
      # path('viewBook/<int:book_id>/', views.viewBook, name='view_book'),

  path('viewBook/<int:book_id>', views.viewBook, name='viewBook'),
 
  # path('verify-email/', views.verify_email, name='verify_email'),
  path('send-verification-email/', views.send_verification_email, name='send_verification_email'),
 
 path('delete_profile/', delete_profile, name='delete_profile'),

 path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
 path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
 path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] 





