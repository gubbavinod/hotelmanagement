from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns=[
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('management/',login_required(views.homepage),name='homepage'),
    path('menu/', login_required(views.menu), name='menu'),
    path('get_cuisine_items/', login_required(views.get_cuisine_items), name='get_cuisine_items'),
    path('order/', login_required(views.order), name='order'),
    path('get_all_items/', login_required(views.get_all_items), name='get_all_items'),
]
