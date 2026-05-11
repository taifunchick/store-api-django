from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('update/<int:pk>/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('remove/<int:pk>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
]