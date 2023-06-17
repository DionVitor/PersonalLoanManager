from rest_framework.serializers import ModelSerializer

from loan.models import LoanField


class LoanFieldSerializer(ModelSerializer):
    class Meta:
        model = LoanField
        fields = ["id", "name"]
