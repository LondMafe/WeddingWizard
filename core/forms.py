from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from datetime import date
from .models import CustomUser, Profile

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'w-full py-2 px-3 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class': 'w-full py-2 px-3 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
    partner1_name = forms.CharField(max_length=100, label="Your name",
                                    widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                  'class': 'w-full py-2 px-3 rounded-xl'}))
    partner2_name = forms.CharField(max_length=100, label="Your partner's name",
                                    widget=forms.TextInput(attrs={'placeholder': 'Your partner\'s name',
                                                                  'class': 'w-full py-2 px-3 rounded-xl'}))
    birth_year1 = forms.IntegerField(label="Your birth year",
                                     widget=forms.NumberInput(attrs={'placeholder': 'Your birth year',
                                                                     'class': 'w-full py-2 px-3 rounded-xl'}))
    birth_year2 = forms.IntegerField(label="Your partner's birth year",
                                     widget=forms.NumberInput(attrs={'placeholder': 'Your partner\'s birth year',
                                                                     'class': 'w-full py-2 px-3 rounded-xl'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'partner1_name', 'partner2_name', 'birth_year1', 'birth_year2')
        
    def clean(self):
        cleaned_data = super().clean()
        birth_year1 = cleaned_data.get("birth_year1")
        birth_year2 = cleaned_data.get("birth_year2")

        if birth_year1 and birth_year2:
            current_year = date.today().year
            age1 = current_year - birth_year1
            age2 = current_year - birth_year2

            if age1 < 18 or age2 < 18:
                self.add_error('birth_year1', "The partners must be at least 18 years old.")
                self.add_error('birth_year2', "The partners must be at least 18 years old.")
                
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                user_type='client',
                partner1_name=self.cleaned_data['partner1_name'],
                partner2_name=self.cleaned_data['partner2_name'],
                birth_year1=self.cleaned_data['birth_year1'],
                birth_year2=self.cleaned_data['birth_year2']
            )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'w-full py-2 px-3 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))

class SignupVendorsForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'w-full py-2 px-3 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class': 'w-full py-2 px-3 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password',
                                                                 'class': 'w-full py-2 px-3 rounded-xl'}))
    name = forms.CharField(max_length=100, label="Vendor's name",
                           widget=forms.TextInput(attrs={'placeholder': 'Vendor\'s name',
                                                         'class': 'w-full py-2 px-3 rounded-xl'}))
    id = forms.IntegerField(label="Vendor's ID",
                            widget=forms.NumberInput(attrs={'placeholder': 'Vendor\'s ID',
                                                            'class': 'w-full py-2 px-3 rounded-xl'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'name', 'id')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                user_type='vendor',
                vendor_name=self.cleaned_data['name'],
                vendor_identifier=self.cleaned_data['id']
            )
        return user

class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Update your email address',
                                                            'class': 'form-control w-full py-2 px-3 rounded-xl'}))

    class Meta:
        model = User
        fields = ['email']
