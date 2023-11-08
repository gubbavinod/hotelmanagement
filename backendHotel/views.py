from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
import csv

from backendHotel.databaseconnection import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to the homepage upon successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

@login_required
def homepage(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'homepage.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,"Logged Out Successfully")
    return redirect('/Hotel/login')  # Redirect to the login page after logging out



def get_cuisine_items(request):
    cuisine = request.GET.get('cuisine')

    items = get_items_by_cuisine(cuisine)
    
    return JsonResponse(items, safe=False)


@login_required
def menu(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        return redirect("menu")
    else:
        return render(request, 'menu.html')
        
@login_required
def order(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'order.html')
    
def get_all_items(request):
    
    # Call the function to get the items
    items = get_items_list()
    
    return JsonResponse(items, safe=False)


