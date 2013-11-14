'''
Created on Nov 11, 2013
Contains all forms
@author: pallavi
'''

from django import forms
from Tkinter import *

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
        bname = forms.CharField(
        label='Board_Name',
        widget=forms.TextInput(attrs={'size': 64})
        )
        bdesc = forms.CharField(
        label='Board_Description',
        widget=forms.TextInput(attrs={'size': 64})
)
