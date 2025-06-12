#here import the view and then set its path, cart/,checkout/ and the view name

from django.urls import path
from . import views

urlpatterns = [
    #leaves the empty string for the base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]