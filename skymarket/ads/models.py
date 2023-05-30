from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1)], verbose_name='Название')
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Цена')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField(verbose_name='Текст', max_length=1000, validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
