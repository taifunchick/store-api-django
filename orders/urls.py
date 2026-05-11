from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='orders'),
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('<int:pk>/cancel/', views.CancelOrderView.as_view(), name='cancel_order'),
]