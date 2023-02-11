from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип')
    description = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Price(models.Model):

    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(default='РУБ', max_length=3, verbose_name='Валюта')

    def __str__(self):
        return 'Цена: {} {}'.format(self.price, self.currency)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Product(models.Model):

    name = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    pr_price = models.ForeignKey(Price, on_delete=models.CASCADE, verbose_name='Цена')
    count = models.IntegerField(default=1, verbose_name='Количество')
    barcode = models.CharField(max_length=9, verbose_name='Штрихкод')
    data_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Тип')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{} | {}'.format(self.name, self.pr_price)
