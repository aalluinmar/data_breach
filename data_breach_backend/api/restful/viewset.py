import json
import logging

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
        DataBreachUploadViewset
    """
    queryset = DataBreach.objects.all().order_by('name')
    serializer_class = DataBreachUploadSerializer
