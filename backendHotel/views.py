from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
import csv



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


@login_required
def menu(request):
    # Your CSV file path
    file_path = '/Users/santhoshnama/Desktop/React/Project/hotelmanagement/backendHotel/meal_info.csv'
    
    # Function to fetch cuisines from the CSV file
    def get_cuisines(file_path):
        cuisines = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Appending cuisine data to the list
                cuisines.append({
                    'name': row['cuisine']  # Image path from the CSV
                })
        return cuisines
    
    cuisine_data = get_cuisines(file_path)
    return render(request, 'menu.html', {'cuisine_data': cuisine_data})



def get_cuisine_items(request):
    cuisine = request.GET.get('cuisine')
    file_path = '/Users/santhoshnama/Desktop/React/Project/hotelmanagement/backendHotel/meal_info.csv'
    cuisine_items = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['cuisine'] == cuisine:
                item_list = cuisine_items.get(row['cuisine'], [])
                item_list.append(row['Item'])
                cuisine_items[row['cuisine']] = item_list

    return JsonResponse(cuisine_items, safe=False)
