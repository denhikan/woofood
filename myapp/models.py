from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

""""Выбор размеров пиццы"""
class Size(models.Model):
    name = models.CharField('Размер', max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

""""Выбор веса пиццы"""
class Weight(models.Model):
    name = models.CharField('Вес', max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Вес"
        verbose_name_plural = "Вес"

"""Категория товара"""
class Category(models.Model):
    title = models.CharField("Название категории", max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

""""Пукнты для выбора типа тесто """
DOUGH_TYPE = [
    ('Традиционное тесто,', 'Традиционное тесто,'),
    ('Тонкое тесто,', 'Тонкое тесто,')
]


""""Модель продуктов"""
class Product(models.Model):
    title = models.CharField('Название товара', max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    descriprion = models.TextField('Описание товара',  max_length=5000)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=0)
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Размер', default=None)
    weight = models.ForeignKey(Weight, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Вес', default=None)
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение в списке')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    testo = models.CharField(null=True, blank=True, choices=DOUGH_TYPE, max_length=100, default=None)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Cart(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
