from rest_framework.viewsets import ModelViewSet

from loan.models import LoanField
from loan.serializers import LoanFieldSerializer


class LoanFieldViewSet(ModelViewSet):
    queryset = LoanField.objects.all()
    serializer_class = LoanFieldSerializer
