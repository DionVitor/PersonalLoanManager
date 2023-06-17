from django.urls import path

from loan.views import LoanFieldViewSet


app_name = "loan"

loan_fields_list = LoanFieldViewSet.as_view({
    "get": "list"
})

urlpatterns = [
    path("loan-fields", loan_fields_list, name="loan-fields-list")
]
