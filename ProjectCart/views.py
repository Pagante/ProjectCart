from django.shortcuts import render
from store.models import Product, reviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = reviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)