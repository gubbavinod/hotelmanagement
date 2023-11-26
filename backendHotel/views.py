from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse

import json

from backendHotel.databaseconnection import *


def set_user_type(request, user_type):
    """
    Helper function to set the user type in the session.
    """

    request.session['user_type'] = user_type

def set_loginStatus(request, user_status):
    """
    Helper function to set the user login status in the session.
    """
    
    request.session['user_status'] = user_status

def set_UserName(request, userName):
    """
    Helper function to set the user Name in the session.
    """
    request.session['userName'] = userName


def signup(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        password = request.POST.get('password')
        username = request.POST.get('username')
        mailid = request.POST.get('mailid')
        phone_number = request.POST.get('phone_number')
        result=insert_customer(customer_name ,username, password, mailid, phone_number)
        if result:
            return redirect('login')  # Redirect to the homepage upon successful login
        else:
            return render(request, 'login', {'error': 'Invalid request'})
    
    return render(request, 'login.html')

def customer_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Replace 'username' with the actual form field name
        password = request.POST.get('password')  # Replace 'password' with the actual form field name

        if customer_authentication(username, password):
            set_user_type(request, 'customer')
            set_loginStatus(request, True)
            set_UserName(request, username)
            return redirect('homepage')  # Redirect to the homepage upon successful login
        else:

            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login')

def manager_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if manager_authentication(username, password):
            set_user_type(request, 'manager')
            set_loginStatus(request, True)
            return redirect('homepage')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')



def homepage(request):
    if request.session.get('user_status',''):
        return render(request, 'homepage.html')  #if the user is not authenticated
    else:
        return redirect("login")



def logout_view(request):
    logout(request)
    set_user_type(request, '')
    set_loginStatus(request,False)
    messages.info(request,"Logged Out Successfully")
    return redirect('/Hotel/login')  # Redirect to the login page after logging out



def get_cuisine_items(request):
    cuisine = request.GET.get('cuisine')

    items = get_items_by_cuisine(cuisine)
    
    return JsonResponse(items, safe=False)



def menu(request):
    if not request.session.get('user_status',''): #if the user is not authenticated
        return redirect("menu")
    else:
        return render(request, 'menu.html')
        

def order(request):
    if not request.session.get('user_status',''): #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'order.html')
    
def get_all_items(request):
    
    # Call the function to get the items
    items = get_items_list()
    
    return JsonResponse(items, safe=False)


def get_pastOrders(request):
    
    # Call the function to get the items
    if(request.session.get('user_type', '') =='customer'):
        username=request.session.get('userName', '')
        items = get_pastOrdersDB(username)
    else:
        items = get_pastOrdersDB()
    return JsonResponse(items, safe=False)



def contactUS(request):
    if not request.session.get('user_status',''):  #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'contactUS.html')


def about(request):
    if not request.session.get('user_status',''):  #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'about.html')


def reservation(request):
    if not request.session.get('user_status',''): #if the user is not authenticated
        return redirect("login")
    else:
        return render(request, 'reservation.html')
    

def placeOrder(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        customer_name = data.get('customerName')
        items = str(data.get('items'))
        totalPrice = data.get('totalPrice')
        # Assuming your `insert_order` function returns a boolean indicating success
        if request.session.get('user_type', '') == 'customer':
            result = insert_order(customer_name, items, request.session.get('userName', ''), totalPrice)
        else:
            result = insert_order(customer_name, items, 'manager', totalPrice)
        
        if result:
            # Return a JSON response indicating success
            return JsonResponse({'status': 'success'})
        else:
            # Return a JSON response indicating failure
            return JsonResponse({'status': 'failure'})
    
    return render(request, 'order.html')