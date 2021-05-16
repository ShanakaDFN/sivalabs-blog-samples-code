from .models import Inventory, Order, OrderDetail, Shipment, ShipmentDetail
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models


class ShipmentDetailInline(admin.TabularInline):
    model = ShipmentDetail
    fields = ('product', 'quantity', 'unit_price', 'amount', 'status')
    ordering = ('product',)


class ShipmentAdmin(admin.ModelAdmin):
    inlines = [ShipmentDetailInline]

    list_display = (
        'shipment_code',
        'volume',
        'product_cost',
        'order_placement_date',
        'preparation_date',
        'loading_date',
        'received_date',
        'status'
        )

    ordering = ('-created_date',)
    
    readonly_fields = (
        'created_date',
        'modified_date',
        )
    fieldsets = ((
        None, {
            'fields': (
                'shipment_code', 
                'type', 
                'supplier',
                'agent',
                'volume',
                'weight',
                'order_placement_date',
                'preparation_date',
                'loading_date',
                'received_date',
                'product_cost',
                'freight_charge',
                'sl_transport_charge',
                'ch_transport_charge',
                'initial_payment',
                'balance_payment',
                'alibaba_initial_charge',
                'alibaba_balance_charge',
                'alibaba_total_charge',
                'stamp_duty',
                'agent_charge',
                'total_shipping_cost',
                'shipping_cost_factor',
                'exchange_rate',
                'status'
                )
        }), (
        'Other Information', {
            'fields': (
                'created_date', 
                'modified_date'
                ),
            'classes': ('collapse',)
        })
    )
    

    class Media:
        js = (
            'sim/js/product_amount.js',
            'admin/js/vendor/jquery/jquery.min.js',
            'admin/js/jquery.init.js'
        )


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'shipment',
        'quantity',
        'cost',
        'retail_price',
        'wholesale_price',
        'warranty_price',
        'status'
        )
    
    readonly_fields = (
        'created_date',
        'modified_date',
        )
    fieldsets = ((
        None, {
            'fields': (
                'product', 
                'shipment', 
                'quantity',
                'cost',
                'retail_price',
                'wholesale_price',
                'warranty_price',
                'status'
                )
        }), (
        'Other Information', {
            'fields': (
                'created_date', 
                'modified_date'
                ),
            'classes': ('collapse',)
        })
    )


admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Order, OrderAdmin)
