from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=99, label=False, widget=forms.NumberInput(attrs={'class': 'quantity input-text', 'name': 'quantity', 'value': '1', 'text-align': 'center'}))

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)