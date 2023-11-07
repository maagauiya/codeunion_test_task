from django_filters import rest_framework as django_filters

from apps.currency.models import Currency


class CurrencyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name")

    class Meta:
        model = Currency
        fields = ['name']
