import logging

from rest_framework import serializers

from api.models import DataBreach


# Get an instance of a logger
logger = logging.getLogger(__name__)

class DataBreachUploadSerializer(serializers.ModelSerializer):
    """
        DataBreachUploadSerializer inherits ModelSerializer. This ModelSerializer
        will perform all necessary operations like insert, update, select,
        delete.
    """

    class Meta:
        model = DataBreach
        exclude = ('audit_status',)
