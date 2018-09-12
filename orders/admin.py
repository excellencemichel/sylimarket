from django.contrib import admin

from .models import Order, ProductPurshase, ProductPurshasePayementLivraison, OrderPayementLivraison

# Register your models here.

admin.site.register(Order)

admin.site.register(ProductPurshase)


admin.site.register(OrderPayementLivraison)
admin.site.register(ProductPurshasePayementLivraison)



