from django.urls import path
from web.views import index, category_detail, product_detail, search_products


app_name = "web"

urlpatterns = [
    path('', index, name="index"),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('search/', search_products, name='search_products'),
]
