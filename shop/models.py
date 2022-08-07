from django.db import models


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
