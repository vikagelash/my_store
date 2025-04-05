from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

def select_product_view(request, pk=None):
    if pk:
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_detail.html', {'product': product})
    else:
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('select_all_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('select_all_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('select_all_products')
    return render(request, 'delete_product.html', {'product': product})






