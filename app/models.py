import ckeditor.fields
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.shortcuts import render
from .tasks import text, printer, hello

class Advertisements(models.Model):
    CATEGORYS =(
        ('Tanks', 'Танк'),
        ('Hily', 'Хилы'),
        ('DD', 'ДД'),
        ('Merchants', 'Торговцы'),
        ('Guild_Masters', 'Гилдмастеры'),
        ('Quest_Givers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potion_Makers', 'Зельевары'),
        ('Spell Masters', 'Мастера_заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    apps_text = ckeditor.fields.RichTextField()
    category = models.CharField(max_length=13, choices=CATEGORYS, default='Tanks')
    apps_datetime = models.DateTimeField(auto_now_add=True)

class Usersresponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.TextField()
    status = models.BooleanField(default=False)
    article = models.ForeignKey(Advertisements, on_delete=models.CASCADE)