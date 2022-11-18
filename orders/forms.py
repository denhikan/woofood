from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={ 'class': 'form__name form__input', 'placeholder': 'Имя клиента'}))
    number_telephone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form__number form__input', 'placeholder': 'Введите номер телефона'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={ 'class': 'form__info form__input'}))
    street = forms.CharField(label='Улица', widget=forms.TextInput(attrs={'class': 'form__info form__input'}))
    house = forms.CharField(label='Дом', widget=forms.TextInput(attrs={'class': 'form__info form__input'}))
    entrance = forms.CharField(label='Подъезд', required=False, widget=forms.TextInput(attrs={'class': 'form__info form__input'}))
    floor = forms.CharField(label='Этаж', required=False, widget=forms.TextInput(attrs={'class': 'form__info form__input'}))
    flat = forms.CharField(label='Квартира', required=False, widget=forms.TextInput(attrs={'class': 'form__info form__input'}))
    class Meta:
        model = Order
        fields = ['first_name',  'number_telephone', 'city', 'street', 'house', 'entrance', 'floor', 'flat']