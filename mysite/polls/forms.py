from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    #to take the input of username
    user_name = forms.CharField(max_length=100)
    # to take the input of password
    password = forms.CharField(max_length=100)
