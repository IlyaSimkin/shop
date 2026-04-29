from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, User, Cart, CartItem

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {'product': product})