from django.db import models

class Order(models.Model):
    description = models.CharField(max_length=256, verbose_name='Детали заказа')
    customer_id = models.IntegerField(null=False, verbose_name='Клиент №')
