from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.orders, name="orders"),

    path('orders/create-order/', views.create_order, name="create-order"),
    path('orders/edit-order/<str:pk>', views.edit_order, name="create-order"),
    path('orders/delete-order/<str:pk>', views.delete_order, name="create-order"),

]
