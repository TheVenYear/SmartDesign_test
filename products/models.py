from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, default='Без названия', verbose_name='название')
    description = models.TextField(max_length=3000, blank=True, verbose_name='описание')

    def __str__(self):
        return f'товар №{self.id}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Parameter(models.Model):
    key = models.CharField(max_length=50, verbose_name='ключ')
    value = models.CharField(max_length=300, verbose_name='значение')
    product = models.ForeignKey(to=Product, related_name='params', verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'параметр'
        verbose_name_plural = 'параметры'
