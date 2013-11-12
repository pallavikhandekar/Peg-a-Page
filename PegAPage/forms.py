'''
Created on Nov 11, 2013
Contains all forms
@author: pallavi
'''

from django import forms
from Tkinter import *

class BookmarkSaveForm(forms.Form):
    url = forms.URLField(
        label='URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'size': 64})
    )
    pegs = forms.CharField(
        label='Pegs',
        required=False,
        widget=forms.TextInput(attrs={'size': 64})
    )
    def browse(self):
        print "browse"
    btnBrowse = Button(text='Browse',command= browse).pack()
    
