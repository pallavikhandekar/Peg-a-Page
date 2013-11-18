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