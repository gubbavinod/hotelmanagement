from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns=[
    path('login/', views.manager_login_view, name='login'),
    path('signup/', views.signup, name='signup'),
     path('customer_login/', views.customer_login_view, name='customer_login'),
    path('logout/', views.logout_view, name='logout'),
    path('management/',views.homepage,name='homepage'),
    path('menu/',views.menu,name='menu'),
    path('get_cuisine_items/', views.get_cuisine_items, name='get_cuisine_items'),
    path('order/', views.order, name='order'),
    path('get_all_items/', views.get_all_items, name='get_all_items'),
    path('get_pastOrders/', views.get_pastOrders, name='get_pastOrders'),
    path('placeOrder/', views.placeOrder, name='placeOrder'),
    path('contactUS/', views.contactUS, name='contactUS'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
]
