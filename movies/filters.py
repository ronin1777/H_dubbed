from django_filters import rest_framework as filters

from movies.models import Movie


class MovieFilters(filters.FilterSet):
    max_year = filters.DateFromToRangeFilter(field_name='end_release_date', lookup_expr='lte')
    range_year = filters.DateRangeFilter(field_name='end_release_date', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['title']
