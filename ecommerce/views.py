from django.shortcuts import render
from store.models import Product, ReviewRating
#from django.contrib import EmailMessage
from django.core.mail import EmailMessage

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    context = {
        'products':products,
        'reviews':reviews,
    }

    return render(request, 'home.html',context)
