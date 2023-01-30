from django.db import models
from django.urls import reverse

class Women(models.Model):  # Wonen = name
    title = models.CharField(max_length=255, verbose_name="Заголовок")   # 'verbose_name' for view in the admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):   # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('post', kwargs={'post_slug': self.slug})   # функция reverse составляет url

    class Meta:
        verbose_name = 'Известные женщины'         # название в админ панели
        verbose_name_plural = 'Известные женщины'  # множ. число в админ панели
        ordering = ['-time_create', 'title']        # сортировка, "-" - обр.порядок. Ordering for view at site


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")   # 'verbose_name' for view in the admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})   # функция reverse составляет url change slug = id, slug = pk

    class Meta:
        verbose_name = 'Категории' # название в админ панели
        verbose_name_plural = "Категории"  # множ. число
        ordering = ['id']

