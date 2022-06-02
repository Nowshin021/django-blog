from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from theblog.models import ProfileModel
from .models import models

class SignupForm (UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    #phone = forms.CharField(max_length=11)


    class Meta :
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')



class EditProfileForm (UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    #last_login =forms.CharField(max_length=100)
    #is_superuser = forms.CharField(max_length=100)
    #is_staff = forms.CharField(max_length=100)
    #is_active = forms.CharField(max_length=100)
    date_joined =forms.CharField(max_length=100)

    #phone = forms.CharField(max_length=11)


    class Meta :
        model = User
        fields = ('username', 'first_name','last_name', 'email','date_joined', 'password')


class AddProfileInformationForm(forms.ModelForm):
    bio=forms.CharField(widget=forms.Textarea)
    class Meta :
        model = ProfileModel
        fields=('bio', 'profile_pic', 'facebook','twitter','instagram','linkedin')


         

class EditInformationForm(UserChangeForm):
    
    class Meta :
        model = ProfileModel
        fields = ('bio', 'profile_pic','facebook', 'twitter','instagram', 'linkedin')