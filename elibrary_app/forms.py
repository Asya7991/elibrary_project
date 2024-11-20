from django import forms
from .models import EBooksModel

class EBooksForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Образование', 'Образование'),
        ('Художественная литература', 'Художественная литература'),
        ('Наука', 'Наука'),
        # Add more categories as needed        
    ]

    category = forms.ChoiceField(label="Категория", choices=CATEGORY_CHOICES)

    class Meta:
        model = EBooksModel
        fields = ['title', 'author_name', 'summary', 'pages', 'pdf', 'category']
        labels = {
            "title": "Название книги",
            "author_name": "Автор",
            "summary":"Краткое содержание",
            "pages":"Количество страниц",
            "pdf":"Пдф",
            "category":"Категория",
        }

    def __init__(self, *args, **kwargs):
        super(EBooksForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название',})
        self.fields['author_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите автора',})
        self.fields['pages'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите количество страниц'})
        self.fields['pdf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Загрузите файл в формате pdf'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите нужную категорию'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'О чём книга?'})
        
        # Make all fields required
        for field_name, field in self.fields.items():
            field.required = True

