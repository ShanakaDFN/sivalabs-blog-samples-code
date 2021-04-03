from .models import Inventory, Invoice, InvoiceDetail, Shipment, ShipmentDetail
from django.contrib import admin


class ShipmentDetailInline(admin.TabularInline):
    model = ShipmentDetail
    readonly_fields = ('amount',)
    fields = ('product', 'quantity', 'unit_price', 'amount', 'status')


class ShipmentAdmin(admin.ModelAdmin):
    inlines = [ShipmentDetailInline]


class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]


admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Inventory)
admin.site.register(Invoice, InvoiceAdmin)
