from .models import Agent, Brand, ContactPerson, Courier, Customer, Model, Product, Stakeholder, Supplier
from django.contrib import admin


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_number', 'email')


class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'email', 'stakeholder')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'inventory_code',
        'oem',
        'hs_code',
        'unit_price'
        )
    search_fields = ['product_name']
    readonly_fields = (
        'created_date',
        'modified_date',
        )
    ordering = ('inventory_code',)
    fieldsets = ((
        None, {
            'fields': (
                'product_name', 
                'tag_name', 
                'inventory_code',
                'oem',
                'hs_code',
                'unit_price',
                'length',
                'width',
                'height',
                'volume',
                'weight',
                'brand',
                'model',
                'image_url',
                'threshold',
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

    def volume(self, obj):
        # return whatever initial value you want
        return obj.length*obj.width*obj.width

    def save_model(self, request, obj, form, change):
        obj.save()


    class Media:
        js = (
            'data/js/product_volume.js',
            'admin/js/vendor/jquery/jquery.min.js',
            'admin/js/jquery.init.js'
        )


admin.site.register(Stakeholder)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Agent)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Brand)
admin.site.register(Model)
