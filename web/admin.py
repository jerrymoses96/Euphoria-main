from django.contrib import admin
from web.models import Product, Category, Gender, Size

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'image']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'brand', 'image', 'price', 'ratings',
                    'comment_count', 'description', 'category', 'gender']


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Gender)

admin.site.register(Size)
