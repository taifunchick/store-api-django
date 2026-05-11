from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'status', 'total_amount', 'shipping_address', 
                  'phone', 'notes', 'items', 'created_at', 'updated_at']
        read_only_fields = ['order_number', 'total_amount', 'created_at']

class CreateOrderSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)