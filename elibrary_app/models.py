from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class EBooksModel(models.Model):
 
    title = models.CharField(max_length = 80)
    summary = models.TextField(max_length=2000)
    pages = models.CharField(max_length=80)
    pdf = models.FileField(upload_to='pdfs/')
    author_name = models.CharField(max_length=80, default="")
    uploader = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    uploader_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"
    

class ConfirmationCode(models.Model):
    email = models.EmailField(unique=True)  # Уникальный email
    code = models.CharField(max_length=36, default=uuid.uuid4)  # Генерация уникального кода
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания кода
    is_used = models.BooleanField(default=False)  # Флаг, использован ли код

def __str__(self):
    return f"Confirmation code for {self.email}: {self.code}"
