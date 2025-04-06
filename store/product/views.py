from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponseForbidden
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer

class AddProductView(APIView):
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to add a product.")

        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})

    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to add a product.")

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)

        return render(request, 'add_product.html', {'form': form})

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products, 'user': request.user})


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return render(request, 'product_detail.html', {'product': serializer.data})


class UpdateProductView(APIView):
    def get(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to update this product.")

        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'update_product.html', {'form': form})

    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to update this product.")

        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            serializer = ProductSerializer(product)
            return redirect('product_detail', pk=product.pk)

        return render(request, 'update_product.html', {'form': form})

class DeleteProductView(APIView):
    def get(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to delete this product.")

        product = get_object_or_404(Product, pk=pk)
        return render(request, 'delete_product.html', {'product': product})

    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to delete this product.")

        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product_list')

