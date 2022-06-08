from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Student(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return str(self.roll_no)