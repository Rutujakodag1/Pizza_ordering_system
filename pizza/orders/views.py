# from django.shortcuts import render

# # Create your views here.

# # views.py
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from .models import Pizza
# from .forms import OrderForm

# def pizza_detail(request, pizza_id):
#     pizza = get_object_or_404(Pizza, id=pizza_id)
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # Handle the order logic here
#             quantity = form.cleaned_data['quantity']
#             total_bill = quantity * pizza.price
#             # Redirect to a success page or display a success message
#             return render(request, 'order_success.html', {'pizza': pizza, 'quantity': quantity, 'total_bill': total_bill})
#     else:
#         form = OrderForm()
#     return render(request, 'pizza_detail.html', {'pizza': pizza, 'form': form})


from django.shortcuts import render, get_object_or_404
from .models import Pizza
from .forms import OrderForm

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_bill = quantity * pizza.price
            return render(request, 'order_success.html', {'pizza': pizza, 'quantity': quantity, 'total_bill': total_bill})
    else:
        form = OrderForm()
    return render(request, 'pizza_detail.html', {'pizza': pizza, 'form': form})

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})
