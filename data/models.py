from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Brand(models.Model):
    brand_name = models.CharField(max_length=150)
    logo_image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    model_name = models.CharField(max_length=150)
    vehicle_image_url = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    tag_name = models.CharField(max_length=150)
    inventory_code = models.CharField(max_length=8)
    oem = models.CharField(max_length=50)
    hs_code = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    volume = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    threshold = models.IntegerField()

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2

    status = models.IntegerField(choices=Status.choices)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Stakeholder(models.Model):
    company_name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    alibaba_profile = models.CharField(max_length=200)
    website = models.CharField(max_length=100)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2

    status = models.IntegerField(choices=Status.choices)

    class Meta:
        abstract = False

    def __str__(self):
        return self.company_name


class Supplier(Stakeholder):
    supplier_code = models.CharField(max_length=6)


class Agent(Stakeholder):
    agent_code = models.CharField(max_length=6)


class Courier(Stakeholder):
    courier_code = models.CharField(max_length=6)


class ContactPerson(models.Model):
    name = models.CharField(max_length=50)
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)
    wechat_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2

    status = models.IntegerField(choices=Status.choices)


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)

    class Type(models.IntegerChoices):
        NORMAL = 0
        WORKSHOP = 1
        SPAREPARTSHOP = 2

    type = models.IntegerField(choices=Type.choices)
    contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=200) 
    email = models.CharField(max_length=100)

    class Status(models.IntegerChoices):
        DELETED = 0
        PENDING = 1
        APPRVED = 2
        BLACKLIST = 3

    status = models.IntegerField(choices=Status.choices)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
