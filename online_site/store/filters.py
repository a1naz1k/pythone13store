from django_filters import FilterSet
from .models import  Product


class ProductFilter(FilterSet):
    class Meta:
        moel = Product
        fields = {
            'category': ['exact'],
            'have': ['exact'],
            'price': ['gt','lt']
        }