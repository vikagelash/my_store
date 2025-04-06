from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

# Add Product View (API logic, but rendering template)
class AddProductView(APIView):
    def get(self, request):
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            # Serialize the saved product object
            serializer = ProductSerializer(product)
            return redirect('product_detail', pk=product.pk)  # Redirect to product detail page after adding

        return render(request, 'add_product.html', {'form': form})


# Product List View (API logic, but rendering template)
# Product List View (API logic, but rendering template)
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products, 'user': request.user})

# Product Detail View (API logic, but rendering template)
class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return render(request, 'product_detail.html', {'product': serializer.data})


# Update Product View (API logic, but rendering template)
class UpdateProductView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'update_product.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            # Serialize the updated product data
            serializer = ProductSerializer(product)
            return redirect('product_detail', pk=product.pk)  # Redirect to product detail page after update

        return render(request, 'update_product.html', {'form': form})


# Delete Product View (API logic, but rendering template)
class DeleteProductView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'delete_product.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product_list')  # Redirect to product list after deletion
