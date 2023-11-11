from rest_framework import filters
from django.db.models.query import QuerySet

from workandservis.models import Workservis


class WorkservisCustomFilter(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset: QuerySet[Workservis], view):
        max_price = request.query_params.get('max_price')
        if max_price:
            return queryset.filter(price__gte=max_price)
        return queryset