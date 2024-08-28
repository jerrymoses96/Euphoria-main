from django.shortcuts import render, get_object_or_404
from web.models import Product, Category, Gender
import random


def index(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    male_gender = Gender.objects.get(name='men')
    female_gender = Gender.objects.get(name='women')

    # Get categories that have products associated with the "Men" gender
    male_categories = Category.objects.filter(
        product__gender=male_gender).distinct()

    # Get categories that have products associated with the "Women" gender
    female_categories = Category.objects.filter(
        product__gender=female_gender).distinct()

    # Convert QuerySet to a list and then shuffle
    categories = list(Category.objects.all())
    random.shuffle(categories)

    # print(categories)

    context = {
        "products": products,
        "categories": categories,
        "male_categories": male_categories,
        "female_categories": female_categories,

    }

    return render(request, "index.html", context=context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,
    }

    return render(request, "category_detail.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    similar_products = Product.objects.filter(
        category=product.category)[:4]
    context = {
        "product": product,
        "similar_products": similar_products
    }

    return render(request, "product_detail.html", context)


def search_products(request):
    query = request.GET.get('q', '')  # Get the search term from the URL
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()  # Return an empty queryset if no query

    print(products)

    context = {
        'products': products,
        'query': query
    }

    return render(request, 'search_detail.html', context)
