
from .models import *
import django_filters

class OrderFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt= django_filters.NumberFilter(field_name="price", lookup_expr= "gt")
    price__lt= django_filters.NumberFilter(field_name="price", lookup_expr= "lt")
    class Meta:
        model = Appartement
        fields = ["city", "is_fork", "period", "size", "tage"]
        
