from django.db import models

# Create your models here.
class Feedback(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(verbose_name="Email")
    descriptions = models.TextField(verbose_name="Сообшение")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio

class Video(models.Model):
    type = models.ForeignKey("Type", on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=255, verbose_name="Заголовка")
    description = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to='./video/', verbose_name='Видеофайл')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    img = models.ImageField(upload_to='video', verbose_name='Фото для обложки', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Type(models.Model):
    img = models.ImageField(upload_to='categories/', null=True, blank=True)
    name = models.CharField(max_length=255)


    def __str__(self):
        return str(self.name)

class User(models.Model):
    img = models.ImageField(upload_to='user/', null=True, blank=True)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)