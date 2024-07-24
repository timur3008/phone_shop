from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    home,
    cart, 
    add_cart, 
    delete_cart, 
    filter_by_memory,
    filter_by_brand,
    get_current_phone,
    filter_by_price,
);

urlpatterns = [
    path('', home, name='home'),
    path('order/<int:order>/', home, name='order'),
    path('cart/', cart, name='cart'),
    path('add-cart/<int:id>/', add_cart, name='add_cart'),
    path('delete-cart/<int:id>/', delete_cart, name='delete_cart'),
    path('filter_by_memory/<int:memory>/', filter_by_memory, name='filter_by_memory'),
    path('filter_by_brand/<str:brand>/', filter_by_brand, name='filter_by_brand'),
    path('filter_by_price/priceFrom=<int:price_from>/priceTo=<int:price_to>/', filter_by_price, name='filter_by_price'),
    path('phone/<int:id>/', get_current_phone, name='get_current_phone'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
