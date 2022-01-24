from django.db import models
from django.db.models import F

from django.urls import reverse


# Вторичная модель
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    # def get_absolute_url(self):
    #     return reverse(viewname='view_news', kwargs={'news_id': self.pk})
    def get_absolute_url(self):
        return reverse(viewname='view_news', kwargs={'pk': self.pk})

    def show_count_view(self):
        news = News.objects.get(pk=self.pk)
        return news.views

    def add_count_view(self):
        self.views = F('views') + 1
        self.save()
        return ''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


# Первичная модель
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наименование категории")

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]


class Feedback(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="Имя")
    contact = models.CharField(max_length=150, blank=True, verbose_name="Контактные данные")
    message = models.TextField(verbose_name="Отзыв")

    def get_absolute_url(self):
        return reverse(viewname='home')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["name"]
