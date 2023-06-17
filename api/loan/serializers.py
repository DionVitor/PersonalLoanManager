from rest_framework.serializers import ModelSerializer, ReadOnlyField

from loan.models import LoanField, LoanOffer


class LoanFieldSerializer(ModelSerializer):
    class Meta:
        model = LoanField
        fields = ["id", "name"]


class LoanOfferSerializer(ModelSerializer):
    id = ReadOnlyField()
    status = ReadOnlyField()

    class Meta:
        model = LoanOffer
        fields = ["id", "status", "answered_fields"]
