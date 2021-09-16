from django.shortcuts import render, redirect
from .models import Product
from cloudipsp import Api, Checkout


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


def buy(request, id):
    product = Product.objects.filter(id=id).get()

    api = Api(merchant_id=1396424,
                  secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(product.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')

    return redirect(url)
