from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from . import forms
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    foods = FoodItem.objects.all()
    # foods = FoodItem.objects.filter(user_name=request.user)
    return render(request, 'index.html',{'foods':foods})

def item_detail(request,pk):
    details = FoodItem.objects.get(id=pk)
    return render(request,'detail.html',{'details':details})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            # Create a new FoodItem instance but do not save it yet
            food_item = form.save(commit=False)
            # Assign the currently logged-in user to the user_name field
            food_item.user_name = request.user
            # Now save the FoodItem instance with the user assigned
            food_item.save()
            return redirect('home')
    else:
        form = forms.AddForm()
    return render(request,'add.html',{'form':form})

@login_required
def edit(request,pk):
    item = FoodItem.objects.get(id=pk)
    form = forms.AddForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'edit.html',{'form':form,'item':item})

@login_required
def delete(request,pk):
    item = FoodItem.objects.get(id=pk)
    item.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success( request,f' Hello {username}. Your account is created')
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request,'profile.html',)


# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...