from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from datetime import date

class SignupForm(UserCreationForm):
    partner1_name = forms.CharField(max_length=100, label="Nombre del integrante 1",
                                    widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                  'class': 'w-full py-2 px-3 rounded-xl'}))
    partner2_name = forms.CharField(max_length=100, label="Nombre del integrante 2",
                                    widget=forms.TextInput(attrs={'placeholder': 'Your partner\'s name',
                                                                  'class': 'w-full py-2 px-3 rounded-xl'}))
    birth_year1 = forms.IntegerField(label="Año de nacimiento",
                                    widget=forms.NumberInput(attrs={'placeholder': 'Your birth year',
                                                                    'class': 'w-full py-2 px-3 rounded-xl'}))
    birth_year2 = forms.IntegerField(label="Año de nacimiento",
                                    widget=forms.NumberInput(attrs={'placeholder': 'Your partner\'s birth year',
                                                                    'class': 'w-full py-2 px-3 rounded-xl'}))
    
    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'partner1_name', 'partner2_name', 'birth_year1', 'birth_year2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                            'class': 'w-full py-2 px-3 rounded-xl'}))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'w-full py-2 px-3 rounded-xl'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))

    def clean(self):
        cleaned_data = super().clean()
        partner1_name = cleaned_data.get("partner1_name")
        partner2_name = cleaned_data.get("partner2_name")
        birth_year1 = cleaned_data.get("birth_year")
        birth_year2 = cleaned_data.get("birth_year")

        if partner1_name == partner2_name:
            self.add_error('partner2_name', "Los nombres de los integrantes deben ser diferentes.")

        current_year = date.today().year
        age1 = current_year - birth_year1
        age2 = current_year - birth_year2

        if age1 < 18 or age2 < 18:
            self.add_error('birth_year', "Las personas deben tener más de 18 años.")
            
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'w-full py-2 px-3 rounded-xl'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
