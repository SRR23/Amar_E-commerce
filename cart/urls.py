
from django.urls import path
from .views import *
urlpatterns = [
   path('cart_list/', Cart_Item.as_view(), name="Cart_Item"),
   path('add_cart/<int:product_id>/', Add_Cart.as_view(), name="Add_Cart"),
   path('add_coupon/', Add_Coupon.as_view(), name="Add_Coupon"),
]