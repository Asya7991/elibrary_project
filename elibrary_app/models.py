from django.db import models
import uuid
from django.utils import timezone


from django.contrib.auth.models import User  # Подключение модели User
from django.db import models
import uuid

class EBooksModel(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=2000)
    pages = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')
    author_name = models.CharField(max_length=80, default="")
    category = models.CharField(max_length=80)

    # Связываем uploader_id с User
    uploader_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='uploaded_ebooks'
    )

    def str(self):
        return f"{self.title}"


class ConfirmationCode(models.Model):
    email = models.EmailField(unique=True)  # Уникальный email
    code = models.CharField(max_length=36, default=uuid.uuid4)  # Генерация уникального кода
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания кода
    is_used = models.BooleanField(default=False)  # Флаг, использован ли код

    def str(self):
        return f"Confirmation code for {self.email}: {self.code}"









# Create your models here.
# class EBooksModel(models.Model):
 
#     title = models.CharField(max_length = 80)
#     summary = models.TextField(max_length=2000)
#     pages = models.CharField(max_length=80)
#     pdf = models.FileField(upload_to='pdfs/')
#     author_name = models.CharField(max_length=80, default="")
#     uploader = models.CharField(max_length=80)
#     category = models.CharField(max_length=80)
#     uploader_id = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.title}"
    

# class ConfirmationCode(models.Model):
#     email = models.EmailField(unique=True)  # Уникальный email
#     code = models.CharField(max_length=36, default=uuid.uuid4)  # Генерация уникального кода
#     created_at = models.DateTimeField(auto_now_add=True)  # Время создания кода
#     is_used = models.BooleanField(default=False)  # Флаг, использован ли код

# def __str__(self):
#     return f"Confirmation code for {self.email}: {self.code}"
