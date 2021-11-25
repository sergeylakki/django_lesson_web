from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

    def my_func(self):
        return 'hello from def'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование категории', db_index=True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def __str__(self):
        return self.title