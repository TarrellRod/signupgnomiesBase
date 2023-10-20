from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from signupgnomies.models import Category, Slot
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','number_of_slots']

class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['slot_holder_firstname','slot_holder_lastname','slot_holder_email','slot_holder_student']
        labels = {'slot_holder_firstname':'First Name',
                  'slot_holder_lastname':'Last Name',
                  'slot_holder_email':'Email',
                  'slot_holder_student':'Student'}