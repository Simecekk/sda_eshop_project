from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse
from shop.models import Product, Cart, ProductReview
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, FormView
from shop.forms import ProductReviewForm


def hello_world_view(request):
    name = request.GET.get("name")
    return HttpResponse(f"Hello world {name}")


# def homepage_view(request):
#     category = request.GET.get("category")
#
#     if category:
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()
#
#     user = get_user_model().objects.first()
#     cart, created = Cart.objects.get_or_create(user=user)
#
#     context = {
#         "products": products,
#         "cart": cart
#     }
#
#     return TemplateResponse(request, "homepage.html", context=context)


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)

        category = self.request.GET.get("category")

        if category:
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()

        user = get_user_model().objects.first()
        cart, created = Cart.objects.get_or_create(user=user)

        context.update({
            "products": products,
            "cart": cart
        })

        return context


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


class ListProductReviewView(FormView):
    template_name = "product_reviews.html"
    form_class = ProductReviewForm

    def get_initial(self):
        product = self.get_object()
        user = get_user_model().objects.first()
        return {"product": product,  "user": user}

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs["product_pk"])

    def get_context_data(self, **kwargs):
        context = super(ListProductReviewView, self).get_context_data(**kwargs)
        product = self.get_object()
        user = get_user_model().objects.first()
        context.update({
            "product": product,
            "cart": user.cart
        })
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        user = get_user_model().objects.first()

        form_data = {
            "user": user.pk,
            "product": product.pk,
            "text": request.POST.get("text"),
            "score": request.POST.get("score")
        }

        bounded_form = ProductReviewForm(data=form_data)
        if not bounded_form.is_valid():
            return JsonResponse(status=400, data={"message": "invalid_data"})

        ProductReview.objects.create(
            user=bounded_form.cleaned_data["user"],
            product=bounded_form.cleaned_data["product"],
            text=bounded_form.cleaned_data["text"],
            score=bounded_form.cleaned_data["score"]
        )

        return self.get(request, *args, **kwargs)
