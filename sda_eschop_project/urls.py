"""sda_eschop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import hello_world_view, add_to_cart_view, cart_view, remove_from_cart_view, HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_world_view, name="hello_world"),
    path("", HomepageView.as_view(), name="homepage"),
    path("add_to_cart/<int:item_pk>/", add_to_cart_view, name="add_to_cart"),
    path("cart/<int:pk>/", cart_view, name="cart_detail"),
    path("remove_from_cart/<int:item_pk>/", remove_from_cart_view, name="remove_from_cart")
]
