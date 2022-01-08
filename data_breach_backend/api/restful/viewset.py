import json
import logging

from django.db.models import Count
from rest_framework import viewsets, serializers
from django.core.serializers.json import DjangoJSONEncoder

from api.models import DataBreach
from api.restful.serializers import DataBreachUploadSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)


def paginating_queryset(self, queryset, request):
        """
            1. Paginate the request and queryset.
            2. Logs the information into log file.
        """
        results = self.paginator.paginate_queryset(queryset, request)
        response = self.paginator.get_paginated_response(
            json.dumps(results, cls=DjangoJSONEncoder)
        )
        response.data['results'] = json.loads(response.data['results'])
        return response


class DataBreachUploadViewset(viewsets.ModelViewSet):
    """
        DataBreachUploadViewset performs all CRUD Operations.
    """
    queryset = DataBreach.objects.all()
    serializer_class = DataBreachUploadSerializer


class BarDataViewset(viewsets.ModelViewSet):
    queryset = DataBreach.objects.all()
    # serializer_class = ProductReviewsSerializer
    def list(self, request):
        query = self.queryset.values('state').annotate(count=Count('individuals_affected', distinct=True))
        return query
