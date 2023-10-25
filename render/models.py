from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt

# Create your models here.
class User(AbstractUser):
    pass

class Journal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = encrypt(models.TextField())
    created_at = models.DateTimeField(auto_now_add=True)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = encrypt(models.TextField())
    details = encrypt(models.TextField(default=""))
    expected_time = models.IntegerField(default=0)
    actual_time = models.IntegerField(default=0)
    day_added = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    posted_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} written by {self.author.username}"
    
class Journal_Prompts(models.Model):
    prompt = models.TextField()

    def __str__(self):
        return f"Journal Prompt: {self.prompt}"

class Youtube_Content(models.Model):
    title = models.TextField()  
    embed_code = models.TextField()
    source = models.TextField()