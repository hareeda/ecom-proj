from django.shortcuts import render
from ecom_app.models import Product, Category
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'products': products})




