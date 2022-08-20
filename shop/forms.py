from django import forms
from django.contrib.auth import get_user_model

from shop.models import Product


class ProductReviewForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), disabled=True)
    score = forms.IntegerField()
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), disabled=True)
    text = forms.CharField(widget=forms.Textarea)
