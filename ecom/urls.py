
from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.home, name="app_home"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
   
] 