from decimal import Decimal
from django.test import TestCase
from receipts.models import Receipt

class ReceiptTest(TestCase):
    fixtures = ["receipts.json", ]

    def test_receipt(self):
        receipt = Receipt.objects.get(id=1)
        total = receipt.total()

        expected = Decimal("12.90")
        self.assertEqual(expected, total)