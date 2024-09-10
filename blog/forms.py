from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'published_date', 'hashtags', 'image', 'image_description', 'color', 'address', 'reference']