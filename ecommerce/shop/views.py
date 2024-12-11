from django.shortcuts import render,redirect
from shop.models import Category
from shop.models import Product
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
# Create your views here.

def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)
def product(request,p):
    c=Category.objects.get(id=p)  #reads a particular record object using id
    p=Product.objects.filter(category=c) # reads a particular category object using id
    context={'cat':c,'product':p}
    return render(request,'product.html',context)
def details(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)
def register(request):
    if (request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if (p == cp):
            u = User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if (request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:login')
def addcategories(request):
    if(request.method == 'POST'):
        na=request.POST['na']
        i=request.FILES['i']
        de=request.POST['de']
        c=Category.objects.create(name=na,image=i,description=de)
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategories.html')


def addproduct(request):
    if(request.method=='POST'):
        na = request.POST['na']
        i = request.FILES['i']
        de = request.POST['de']
        s=request.POST['st']
        p=request.POST['pr']
        c=request.POST['cat']
        c=Category.objects.get(name=c)
        p=Product.objects.create(name=na,image=i,desc=de,stock=s,price=p,category=c)
        p.save()
        return redirect('shop:categories')
    return render(request, 'addproduct.html')


def addstock(request,i):
    p=Product.objects.get(id=i)
    if(request.method =='POST'):
        p.stock=request.POST['ad']
        p.save()
        return redirect('shop:details',i)
    context={'pro':p}
    return render(request,'addstock.html',context)

