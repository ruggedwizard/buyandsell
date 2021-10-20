from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . models import Product
from . forms import ReviewForm, ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def Index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(name__icontains=q)
    context = {'products':products}
    return render(request,'base/index.html', context)

def Detail(request, pk):
    single_product = Product.objects.get(id=pk)
    review_form = ReviewForm()
    related_item = Product.objects.filter(category=single_product.category)
    
    context = {'single_product':single_product,
               'review_form':review_form,
               'category':related_item                                 
                                                }
    return render(request,'base/Product.html',context)

@login_required(login_url='login-page')
def Addproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid:
            product =form.save(commit=False)
            product.posted_by = request.user
            product.save()
            return redirect(Index)
    context = {'form':form, }
    return render(request,'base/add.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username= username, password = password)
        try:
            login(request, user)
            return redirect('landing-page')
        except:
            messages.error(request, "Email or Password is incorrect")
    return render(request,'base/login.html')

def Logout(request):
    logout(request)
    return redirect('landing-page')

def Register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('landing-page')
        else:
           HttpResponse("An Error has Occured!!")
    context = {'form':form}
    return render(request, 'base/register.html', context)