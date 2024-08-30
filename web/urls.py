from django.urls import path
from web.views import index, profile, category_detail, product_detail, search_products, wishlist, add_to_wishlist, cart, add_to_cart, login_view, logout_view


app_name = "web"

urlpatterns = [
    path('', index, name="index"),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('search/', search_products, name='search_products'),
    path('wishlist/', wishlist, name="wishlist"),
    path('add_to_wishlist/<int:product_id>/',
         add_to_wishlist, name='add_to_wishlist'),
    path('cart/', cart, name="cart"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),

]
