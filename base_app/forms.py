from django import forms
from django.core.exceptions import ValidationError
from base_app.models import *


class addApartametForm(forms.ModelForm):
    class Meta:
        model = Apartament
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addHomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addPlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addOfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addGarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addMagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class addOtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


def password_validation(value):
    if len(value) <= 6:
        raise ValidationError("Hasło powinno zawierać co najmniej 6 znaków")


class SearchForm(forms.Form):
    title = forms.CharField(label= "Wyszukiwanie",widget=forms.TextInput(attrs={'class':'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Użytkownik', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Użytkownik', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(validators=[password_validation], label='Hasło', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    re_password = forms.CharField(label='Potwiedź hasło', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='e-mail',widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=False, label='Imię',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False, label='Nazwisko',widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['re_password']:
                raise ValidationError("Hasła nie są identyczne")
        return self.cleaned_data


