from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

# View for displaying all products or product detail based on pk
def select_product_view(request, pk=None):
    if pk:
        # Display the details of a specific product
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_detail.html', {'product': product})
    else:
        # Display all products
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products, 'user': request.user})

# View for adding a new product
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Add product view
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect after successful product creation
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View for updating an existing product
def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after update
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})

# View for deleting a product
def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to the product list after deletion
    return render(request, 'delete_product.html', {'product': product})


from django.shortcuts import render
from django.contrib.auth.models import User  # Assuming you're using the default User model
