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
