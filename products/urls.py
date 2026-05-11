from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('', views.ProductList.as_view(), name='products'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<slug:slug>/reviews/', views.ReviewCreate.as_view(), name='add_review'),
    path('wishlist/', views.WishlistList.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', views.WishlistDelete.as_view(), name='wishlist_delete'),
]