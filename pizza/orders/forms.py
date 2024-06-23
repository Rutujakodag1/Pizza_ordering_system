# # forms.py
# from django import forms

# class OrderForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1, label='Quantity')

from django import forms

class OrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
