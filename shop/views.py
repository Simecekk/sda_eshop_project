from django.http import HttpResponse
from django.template.response import TemplateResponse
from shop.models import Product


def hello_world_view(request):
    name = request.GET.get("name")
    return HttpResponse(f"Hello world {name}")


def homepage_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return TemplateResponse(request, "homepage.html", context=context)
