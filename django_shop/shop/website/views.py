from django.shortcuts import render, redirect
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'website/index.html', context)


def about(request):
    return render(request, 'website/about.html')


def create(request):
    # Необходима валидация.
    if request.method == 'POST':
        product = Product(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price')
        )
        product.save()
    return render(request, 'website/create.html')


def delete(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('website:index')
