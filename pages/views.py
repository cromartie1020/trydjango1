from django.shortcuts import render
from products import views
from products.models import Product
def home(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    print(request.headers)
    products=Product.objects.all()

    context={
        'products':products
    }

    return render(request,'pages/home.html', context)
    
