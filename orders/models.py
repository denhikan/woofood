from django.db import models
from myapp.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    number_telephone = models.CharField(max_length=20, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=250, verbose_name='Улица')
    house = models.CharField(max_length=250, verbose_name='Дом')
    entrance = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Подьезд')
    floor = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Этаж')
    flat = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Квартира')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity