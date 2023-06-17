from random import randint

from infra.celery_gateway.worker import app
from loan.models import LoanOffer


@app.task()
def process_personal_loan(loan_offer_id: str):
    LoanOffer.objects.filter(id=loan_offer_id).update(status=randint(1, 2))
    return True
