from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from web.models import Product, Category, Gender, Wishlist, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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


@login_required
def wishlist(request):

    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        "wishlist_items": wishlist_items,
    }
    return render(request, 'wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)

    response = {
        'status': 'success',
        'message': 'Product added to wishlist' if created else 'Product already in wishlist'
    }
    return JsonResponse(response)


@login_required
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    context = {
        'cart_items': cart_items

    }
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(
        user=request.user, product=product)

    response = {
        'status': 'success',
        'message': 'Product added to cart' if created else 'Product already in cart'
    }
    return JsonResponse(response)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'success': True, 'logged_in': True, 'redirect_url': reverse('web:index')})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})
    else:
        form = AuthenticationForm()

    return render(request, 'index.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('web:index')


@login_required
def profile(request):
    # Example: Retrieve orders for the user (assuming an Order model exists) # Get cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)
    cart_count = cart_items.count()
    cart_product_names = [item.product.name for item in cart_items]

    # Get wishlist items for the logged-in user
    wishlist_items = Wishlist.objects.filter(user=request.user)
    wishlist_count = wishlist_items.count()
    wishlist_product_names = [item.product.name for item in wishlist_items]

    if request.method == 'POST':
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Email updated successfully!')

        if new_password:
            # Check if the new password is valid, e.g., meet certain criteria
            if len(new_password) < 8:
                messages.error(
                    request, 'Password must be at least 8 characters long.')
            else:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Password changed successfully!')
                # Redirect user to login after password change
                return redirect('web:index')

    context = {

        "cart_count": cart_count,
        "cart_product_names": cart_product_names,
        "wishlist_count": wishlist_count,
        "wishlist_product_names": wishlist_product_names,
    }

    return render(request, 'User_profile.html', context=context)
