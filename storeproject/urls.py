from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home_view(request):
    return JsonResponse({
        'message': 'Store API is running!',
        'endpoints': {
            'admin': '/admin/',
            'api/token': '/api/token/',
            'api/token/refresh': '/api/token/refresh/',
            'api/accounts': '/api/accounts/',
            'api/products': '/api/products/',
            'api/cart': '/api/cart/',
            'api/orders': '/api/orders/',
        }
    })

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)