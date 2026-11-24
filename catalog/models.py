from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")

    def __str__(self):
        return f'{self.name}: {self.price}'

    class Meta:
        db_table = 'product'
        ordering = ['name']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
