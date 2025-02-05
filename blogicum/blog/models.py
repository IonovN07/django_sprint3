from core.models import BasePublishedModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(BasePublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True, 
        verbose_name='Идентификатор', 
        help_text='Идентификатор страницы для URL;' 
                'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )

    class Meta():
        verbose_name = 'категории'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title

class Location(BasePublishedModel):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
    
    def __str__(self):
        return self.name
    
class Post(BasePublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем —'
                'можно делать отложенные публикации.'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts_author',
        verbose_name='Автор публикации'         
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts_by_location',
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts_in_category',
        verbose_name='Категория'
    )
    
    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
