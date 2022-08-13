from django.http import HttpResponse
from django.template.response import TemplateResponse
from shop.models import Product


def hello_world_view(request):
    name = request.GET.get("name")
    return HttpResponse(f"Hello world {name}")


def homepage_view(request):
    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    context = {
        "products": products,
        "page_title": "LevneTelefony.cz"
    }

    return TemplateResponse(request, "homepage.html", context=context)
