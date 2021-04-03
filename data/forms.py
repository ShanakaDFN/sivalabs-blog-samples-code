from django import forms
from .models import Product
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' # Or a list of the fields that you want to include in your form

    def clean_created_by(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']

    def clean_modified_by(self):
        if not self.cleaned_data['modified_by']:
            return User()
        return self.cleaned_data['modified_by']
