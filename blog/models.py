from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    hashtags = models.CharField(max_length=200, blank=True, help_text="Ingrese hashtags separados por comas")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Nuevo campo para la imagen

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_hashtags(self):
        return [tag.strip() for tag in self.hashtags.split(',') if tag.strip()]