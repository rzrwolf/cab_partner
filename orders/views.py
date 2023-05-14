from django.shortcuts import render

# Create your views here.
def create_order(request):

    return render(request, 'orders/create-order.html')




def edit_order(request):
    return None


def delete_order(request):
    return None


def orders(request):
    return render(request, 'all-orders.html')