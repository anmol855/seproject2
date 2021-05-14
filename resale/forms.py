from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product,Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class CreateUserForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone']

class CreateProductFrom(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17, required=True)

    title = forms.CharField(max_length=255, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=64, required=True)

    class Meta:
        model = Product
        fields = ['title', 'body', 'phone', 'email', 'product_image', 'name', 'price', 'category','condition','brand']
        widgets = {
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
        }