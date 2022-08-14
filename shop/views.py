from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from shop.models import Product, Cart
from django.contrib.auth import get_user_model


def hello_world_view(request):
    name = request.GET.get("name")
    return HttpResponse(f"Hello world {name}")


def homepage_view(request):
    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    user = get_user_model().objects.first()
    cart, created = Cart.objects.get_or_create(user=user)

    context = {
        "products": products,
        "cart": cart
    }

    return TemplateResponse(request, "homepage.html", context=context)


def add_to_cart_view(request, item_pk):
    product = get_object_or_404(Product, pk=item_pk)
    user = get_user_model().objects.first()
    cart, created = Cart.objects.get_or_create(user=user)
    cart.products.add(product)
    return redirect(request.META.get('HTTP_REFERER', 'homepage'))


def remove_from_cart_view(request, item_pk):
    product = get_object_or_404(Product, pk=item_pk)
    user = get_user_model().objects.first()
    cart, created = Cart.objects.get_or_create(user=user)
    cart.products.remove(product)
    return redirect(request.META.get('HTTP_REFERER', 'homepage'))


def cart_view(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    context = {
        "cart": cart
    }
    return TemplateResponse(request, "cart.html", context=context)
