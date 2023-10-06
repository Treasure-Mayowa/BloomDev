from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Journal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default=f"Entry #{id}", max_length=35)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    details = models.TextField()
    expected_time = models.IntegerField(default=0)
    actual_time = models.IntegerField(default=0)
    day_added = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    posted_by = models.DateTimeField(auto_now_add=True)

class Journal_Prompts(models.Model):
    prompt = models.TextField()