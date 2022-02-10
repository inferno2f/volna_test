from django.contrib import admin

from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer_id', 'description')
    search_fields = ('customer_id',)
    empty_value_display = '-пусто-'


admin.site.register(Order, OrderAdmin)
