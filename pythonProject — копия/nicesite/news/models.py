from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank = True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now = True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default = True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def my_func(self):
        return 'Hello from model'


# Create your models here.
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Новость'   #переименовывает
        verbose_name_plural = 'Новости'   #убирает S в названии
        ordering = ['id']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


