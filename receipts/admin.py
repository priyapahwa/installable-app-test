from django.contrib import admin
from receipts.models import Item, Receipt

admin.site.register(Receipt)
admin.site.register(Item)
