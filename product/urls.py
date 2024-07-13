from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('product_details/<str:slug>/', Product_details.as_view(), name="Product_details"),
    path('category_details/<str:slug>/', Category_details.as_view(), name="Category_details"),
    path('product_lists/', Product_Lists.as_view(), name="Product_Lists"),
    path('search_products/', Search_Products.as_view(), name="Search_Products"),
]