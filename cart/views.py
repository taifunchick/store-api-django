from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(id=product_id, is_active=True)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        quantity = request.data.get('quantity')
        if quantity and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        elif quantity == 0:
            cart_item.delete()
            return Response({'message': 'Item removed'}, status=status.HTTP_200_OK)
        
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
            cart_item.delete()
            return Response({'message': 'Item removed'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)