from django.urls import path
from . import views
from .views import deleteBook

from .views import verify_email, send_verification_email


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
  path('viewBook/<int:book_id>', views.viewBook, name='viewBook'),
  path('viewBook/<int:book_id>', views.viewBook, name='viewBook'),
 

  path('verify-email/', views.verify_email, name='verify_email'),
  path('send-verification-email/', views.send_verification_email, name='send_verification_email'),



  # path('verify-email/', verify_email, name='verify_email'),
  # path('verify-code/', verify_code, name='verify_code'),
  # path('register/', register, name='register'),
  
  # path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
  # path('send_confirmation_code', views.send_confirmation_code, name='send_confirmation_code'),
  # path('send_email', views.send_email, name='send_email'),
  # path('verify_confirmation_code', views.verify_confirmation_code, name='verify_confirmation_code'),
] 





