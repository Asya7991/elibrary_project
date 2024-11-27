from django import forms
from .models import EBooksModel

class EBooksForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Художественная литература', 'Художественная литература'),
        ('Образование', 'Образование'),       
<<<<<<< HEAD
        ('Наука', 'Наука'),           
=======
        ('Наука', 'Наука'),
        # Add more categories as needed        
>>>>>>> ee8bc57db7e8fc09166f0be4d402d3880be3d4ef
    ]

    category = forms.ChoiceField(label="Категория", choices=CATEGORY_CHOICES)

    class Meta:
        model = EBooksModel
        fields = ['title', 'author_name', 'summary', 'pages', 'pdf', 'category']
        labels = {
            "title": "Название книги",
            "author_name": "Автор книги",
            "summary":"Краткое содержание",
            "pages":"Количество страниц",
<<<<<<< HEAD
            "pdf":"Загрузите файл",
=======
            "pdf":"Загрузить книгу",
>>>>>>> ee8bc57db7e8fc09166f0be4d402d3880be3d4ef
            "category":"Категория",
        }

    def __init__(self, *args, **kwargs):
        super(EBooksForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название',})
        self.fields['author_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите автора',})
        self.fields['pages'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите количество страниц'})
        self.fields['pdf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Загрузите файл'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите нужную категорию'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите содержание'})
        
        # Make all fields required
        for field_name, field in self.fields.items():
            field.required = True

