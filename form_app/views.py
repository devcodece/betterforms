from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,TemplateView
from . forms import ProductSkuProductForm
from django.urls import reverse
# Create your views here.

class NewProduct(CreateView):
    form_class = ProductSkuProductForm
    templane_name = 'form-product.html'

    def from_valid(self, form):
        product = form['product'].save()
        sku = form['sku'].save(commit=False)
        sku.product = product
        product.save()
        return HttpResponseRedirect(reverse('success'))

class Success(TemplateView):
    templane_name = 'success.html'

        
