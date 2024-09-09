from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'published_date', 'hashtags']
        widgets = {
            'published_date': forms.DateTimeInput(attrs={
                'type': 'text',  # Flatpickr usa 'text' para mostrar el calendario
                'class': 'form-control datetimepicker',  # Clase para aplicar Flatpickr
            }),
        }
