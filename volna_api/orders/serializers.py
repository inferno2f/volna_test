from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Order
    
    def validate(self, data):
        if data['customer_id'] != 1:
            raise serializers.ValidationError('По ТЗ только единица является валидным айди')
        return data
