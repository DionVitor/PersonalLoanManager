from django.urls import path

from loan.views import LoanFieldViewSet, LoanOfferViewSet


app_name = "loan"

loan_fields_list = LoanFieldViewSet.as_view({
    "get": "list"
})

loan_offer_create = LoanOfferViewSet.as_view({
    "post": "create"
})

urlpatterns = [
    path("loan-fields", loan_fields_list, name="loan-fields-list"),
    path("loan-offer", loan_offer_create, name="loan-offer-create")
]
