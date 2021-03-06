import django_filters
from .models import Viaje

class ProductFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')
    #origen =  django_filters.CharFilter(lookup_expr='icontains')
    #destino =  django_filters.CharFilter(lookup_expr='icontains')
    
    pecio_gt = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_lt = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')

    class Meta:
        model = Viaje
        fields = ['ruta','fecha',]