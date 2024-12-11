from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def search(request):
    p=None
    query=""
    if(request.method=='POST'):
        query=request.POST.get('q')  #read the query
        if query:
            p=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))  #filter the record matching with query
    context={'pro':p,'query':query}
    return render(request,'search.html',context)