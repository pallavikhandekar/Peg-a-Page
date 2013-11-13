'''
Created on Nov 11, 2013
Contains all forms
@author: pallavi
'''

from django import forms
from Tkinter import *

class BookmarkCreateForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'size': 64})
    )
    pegs = forms.CharField(
        label='Pegs',
        required=False,
        widget=forms.TextInput(attrs={'size': 64})
    )
