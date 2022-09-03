from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from shop.models import Product, HelpdeskContact, ProductReview


def error_in_text_validator(value):
    if "error" in value:
        raise ValidationError("Text contains error")


class ProductReviewForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    score = forms.IntegerField(min_value=0, max_value=10)
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all())
    text = forms.CharField(widget=forms.Textarea, validators=[error_in_text_validator, ])

    def clean_text(self):
        value = self.data["text"].replace("sprosty", "******")
        return value


class ProductReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ("score", "text")


class HelpdeskContactForm(forms.ModelForm):
    class Meta:
        model = HelpdeskContact
        fields = ("email", "title", "text")
        # exclude = ("solved", )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
