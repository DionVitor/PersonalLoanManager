from uuid import uuid4
from enum import IntEnum

from django.db import models


class LoanStatus(IntEnum):
    PENDING = 0
    APPROVED = 1
    REJECTED = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class LoanField(models.Model):
    """
    Class designated to describe a field that a loan offer should have.
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LoanOffer(models.Model):
    """
    Class designated to describe an offer for a loan.
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    status = models.IntegerField(choices=LoanStatus.choices(), default=LoanStatus.PENDING)
    answered_fields = models.JSONField(default=dict)

    def get_loan_offer_status(self):
        return LoanStatus(self.status).name.title()

    def __str__(self):
        return f"Loan offer {self.id}"
