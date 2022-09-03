from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from decimal import Decimal


class Product(models.Model):
    CATEGORY_PHONE = "phone"
    CATEGORY_LAPTOP = "laptop"
    CATEGORY_TABLET = "tablet"

    CATEGORY_CHOICES = (
        (CATEGORY_PHONE, "phone"),  # (DB_CODE, "human_readable_name")
        (CATEGORY_LAPTOP, "laptop"),
        (CATEGORY_TABLET, "tablet")
    )

    title = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=10, max_digits=20)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=256)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} : {self.id}"


class Cart(models.Model):
    products = models.ManyToManyField(
        Product, related_name="carts",
    )
    user = models.OneToOneField(
        get_user_model(),
        related_name="cart",
        on_delete=models.CASCADE
    )

    @property
    def total_price(self):
        total_price = Decimal("0")
        for product in self.products.all():
            total_price += product.price
        return total_price


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews",
        on_delete=models.CASCADE
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    user = models.ForeignKey(
        get_user_model(), related_name="user_reviews",
        on_delete=models.CASCADE
    )
    text = models.TextField()


class HelpdeskContact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=512)
    text = models.TextField()
    solved = models.BooleanField(default=False)

