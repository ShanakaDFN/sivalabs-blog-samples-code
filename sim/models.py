from data.models import Supplier, Agent, Customer, Product
from django.db import models


class Shipment(models.Model):
    shipment_code = models.CharField(max_length=10)

    class Type(models.IntegerChoices):
        LOCAL = 0
        AIR = 1
        SEA = 2

    type = models.IntegerField(choices=Type.choices)
    supplier = models.OneToOneField(
        Supplier,
        on_delete=models.CASCADE,
    )
    agent = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
    )
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    order_placement_date = models.DateField()
    preparation_date = models.DateField()
    loading_date = models.DateField()
    received_date = models.DateField()
    product_cost = models.DecimalField(max_digits=6, decimal_places=2)
    freight_Charge = models.DecimalField(max_digits=6, decimal_places=2)
    sl_transport_charge = models.DecimalField(max_digits=6, decimal_places=2)
    ch_transport_charge = models.DecimalField(max_digits=6, decimal_places=2)
    initial_payment = models.DecimalField(max_digits=6, decimal_places=2)
    balance_payment = models.DecimalField(max_digits=6, decimal_places=2)
    alibaba_initial_charge = models.DecimalField(max_digits=6, decimal_places=2)
    alibaba_balance_charge = models.DecimalField(max_digits=6, decimal_places=2)
    alibaba_total_charge = models.DecimalField(max_digits=6, decimal_places=2)
    stamp_duty = models.DecimalField(max_digits=6, decimal_places=2)
    total_shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost_factor = models.DecimalField(max_digits=6, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=6, decimal_places=2)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        SHIPPED = 2
        RECEIVED = 3
        APPRVED = 4
        CLOSE = 5

    status = models.IntegerField(choices=Status.choices)
    created_by = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=20)
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.shipment_code


class ShipmentDetail(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    #@property
    #def get_amount(self):
        #return self.quantity * self.unit_price
    #amount = property(get_amount)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2
        CLOSE = 3

    status = models.IntegerField(choices=Status.choices)

    def __str__(self):
        return self.shipment, self.product


class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )

    shipment = models.OneToOneField(
        Shipment,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField(default=0)
    product_cost = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    warranty_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2
        CLOSE = 3

    status = models.IntegerField(choices=Status.choices)
    created_by = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=20)
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.shipment, self.product, self.quantity


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=6)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
    )
    contact_no = models.CharField(max_length=10)
    note = models.CharField(max_length=100)
    payment_date = models.DateField()

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        CLOSE = 2

    status = models.IntegerField(choices=Status.choices)
    created_by = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_by = models.CharField(max_length=20)
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.invoice_no


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.invoice