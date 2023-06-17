from rest_framework.viewsets import ModelViewSet

from loan.models import LoanField, LoanOffer
from loan.serializers import LoanFieldSerializer, LoanOfferSerializer


class LoanFieldViewSet(ModelViewSet):
    queryset = LoanField.objects.all()
    serializer_class = LoanFieldSerializer


class LoanOfferViewSet(ModelViewSet):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer
