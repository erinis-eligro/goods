from django import forms

class SeachGoodsForm(forms.Form):
    fullname = forms.TextInput()
    email = forms.EmailInput()
