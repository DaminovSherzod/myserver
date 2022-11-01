from itertools import product
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse, HttpResponse
# from django.http import HttpResponse
# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def convert_to_json(product):
    """
    Convert a product to a JSON object
    args:
        product: a product object
    returns:
        a JSON object
    """
    product_json = {
        'id': product.id,
        'name': product.name,
        'company': product.company,
        'color': product.color,
        'RAM': product.RAM,
        'memory': product.memory,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'img_url': product.img_url,
    }
    return product_json

def add_product(request):
    """
    Create a product
    args:
        request: the request object
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST['name'],
            company=request.POST['company'],
            color=request.POST['color'],
            RAM=request.POST['RAM'],
            memory=request.POST['memory'],
            price=request.POST['price'],
            img_url=request.POST['img_url']
        )
        product_json = convert_to_json(product)
        product.save()

        return JsonResponse({'product' : product_json})

    return JsonResponse({'product': {}})

def get_all_company(request):
    """
    Get all companies
    args:
        request: the request object
    return:
        JsonResponse: the list of companies
    """
    companies = Product.objects.all()
    # Get unique companies
    companies = set([company.company for company in companies])

    context = {
        'companies': companies,
        'title': 'Companies'
    }
    return render(request, 'home.html', context)