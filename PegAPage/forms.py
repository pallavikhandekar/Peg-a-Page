'''
Created on Nov 11, 2013
Contains all forms
@author: pallavi
'''
import re
from django import forms
from Tkinter import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
                                label='Password',
                                widget=forms.PasswordInput()
                                )
    password2 = forms.CharField(
                                label='Password (Again)',
                                widget=forms.PasswordInput()
                                )  
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email is already taken.')
    
    

class PegCreateForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'size': 64})
    )
    desc = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'size': 64})
)
    
class BoardCreateForm(forms.Form):    
        name = forms.CharField(
        label='Board_Name',
        widget=forms.TextInput(attrs={'size': 64})
        )
        desc = forms.CharField(
        label='Board_Description',
        widget=forms.TextInput(attrs={'size': 64})
)
        
class CommentPegForm(forms.Form):
        commentdesc = forms.CharField(
        label='Comment Here',
        widget=forms.TextInput(attrs={'size':64})
        )
        
class PegItForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'size': 64})
    )
    desc = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'size': 64})
    )
    bname = forms.CharField(
        label='Board_Name',
        widget=forms.TextInput(attrs={'size': 64})        
)
class LikePegForm(forms.Form):
 url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'size': 64})
    )       
