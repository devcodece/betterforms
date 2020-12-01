from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from . models import CdtBrand, CdtVendor, CdtColor, CdtProductPhoto, TdtProduct

class TdtProductForm(ModelForm):
    class Meta:
        model = TdtProduct
        fields = '__all__'

class TdtSkuProductForm(ModelForm):
    class Meta:
        model = TdtSkuProduct
        fields = ['sku','id_size','quantity','price']

class ProductSkuProductForm(MultiModelForm):
    form_classes = {
        'product':TdtProductForm,
        'sku':TdtSkuProductForm,
    }


