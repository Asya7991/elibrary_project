from django.shortcuts import redirect, render
from elibrary_app.forms import EBooksForm
from elibrary_app.models import EBooksModel
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import ConfirmationCode
import random

# Create your views here.
def Registers(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['first--name']
        lastName = request.POST['last--name']
        
        # Check if a user with the same username already exists
        if User.objects.filter(username=email).exists():
            messages.info(request, 'Такой пользователь уже существует')
            return render(request, 'register.html')  # Не передаем messages в контекст
        else:
            # Create a new user
            register = User.objects.create_user(username=email, password=password, first_name=firstName, last_name=lastName)
            return redirect('login')
    else:
        return render(request, 'register.html') 
    


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            print('Пользователь успешно зарегистрировался')
            return redirect('home')
        else:
            messages.info(request,'Неверные учётные данные. Попробуйте ещё раз.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def home(request):
   return render(request, 'home.html')


def explore(request):
    edu_books = EBooksModel.objects.filter(category='Образование').order_by('title')
    fiction_books = EBooksModel.objects.filter(category='Художественная литература').order_by('title')
    science_books = EBooksModel.objects.filter(category='Наука').order_by('title')
    return render(request, 'explore.html', {'edu_books': edu_books, 'fiction_books': fiction_books, 'science_books': science_books})


@login_required
def addBook(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = EBooksForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = user.first_name + " " + user.last_name
            book.uploader_id = user
            print(book.author)
            book.save()
            print()
            print()
            print(book.author)
            print("Книга успешна загружена")
            print()
            print()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EBooksForm()
    return render(request, 'addBook.html', {'form': form})


def contri(request, user_id):
    user = User.objects.get(id=user_id)
    books = EBooksModel.objects.filter(uploader_id=user)
    print(f"Найдено книг: {books.count()}")
    return render(request, 'contri.html', {'books': books})


def logout(request):
    auth.logout(request)
    return redirect('home')



from django.shortcuts import get_object_or_404
from django.contrib import messages

def deleteBook(request, book_id):
    print(f"Попытка удалить книгу с ID: {book_id}")
    book = get_object_or_404(EBooksModel, id=book_id)
    book.delete()
    messages.success(request, "Книга успешно удалена.")
    print("Книга удалена.")
    return redirect('home')




def editBook(request,book_id):
    book = EBooksModel.objects.get(id=book_id)
    if request.method == 'POST':
        form = EBooksForm(request.POST, request.FILES,instance=book)
        if form.is_valid():
            form.save()
            print()
            print()
            print("Книга успешна загружена")
            print()
            print()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EBooksForm(instance=book)
    return render(request, 'editBook.html', {'form': form,'book':book})

from django.shortcuts import get_object_or_404

def viewBook(request, book_id):
    book = get_object_or_404(EBooksModel, id=book_id)
    book.summary = book.summary.replace('\n', '<br/>')
    return render(request, 'viewBook.html', {'book': book})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import EBooksModel  





from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import random

def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            verification_code = generate_verification_code()
            # Сохраняем код в сессии
            request.session['verification_code'] = verification_code
            request.session['email'] = email
            
            # Отправляем email
            try:
                send_mail(
                    'Email Verification',
                    f'Your verification code is: {verification_code}',
                    settings.EMAIL_HOST_USER,  # используем email из настроек
                    [email],
                    fail_silently=False,
                )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                print(f"Error sending email: {e}")  # для отладки
                return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('code')
        
        if not email or not code:
            return render(request, 'elibrary_app/verify_email.html', {'error': 'Please provide both email and verification code'})
        
        stored_code = request.session.get('verification_code')
        stored_email = request.session.get('email')
        
        if email == stored_email and code == stored_code:
            # Код верификации правильный
            return redirect('register')  # Переход к существующей странице регистрации
        else:
            messages.error(request, 'Неверный код. Попробуйте снова.')
            return render(request, 'elibrary_app/verify_email.html')
    
    return render(request, 'elibrary_app/verify_email.html')






from django.shortcuts import render

def login_view(request):
    return render(request, 'elibrary_app/login.html')

def pong(request):
    return JsonResponse({"message": "pong"})



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Удаляем пользователя
        return redirect('home')  # Перенаправляем на главную страницу
    return redirect('home')  # Если не POST, перенаправляем на главную


