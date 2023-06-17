from rest_framework.viewsets import ModelViewSet

from loan.models import LoanField, LoanOffer
from loan.serializers import LoanFieldSerializer, LoanOfferSerializer

from infra.celery_gateway.tasks import process_personal_loan


class LoanFieldViewSet(ModelViewSet):
    queryset = LoanField.objects.all()
    serializer_class = LoanFieldSerializer


class LoanOfferViewSet(ModelViewSet):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer

    def create(self, request, *args, **kwargs):
        create_response = super(LoanOfferViewSet, self).create(request, *args, **kwargs)
        process_personal_loan.apply_async(
            kwargs={"loan_offer_id": str(create_response.data.get("id"))}
        )
        return create_response
