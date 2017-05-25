from django import forms
from .models import Employer
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()


class UserLoginForm(forms.Form):
    # to take the input of username
    username = forms.CharField()
    # to take the input of password and the widget will hide the text
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user no longer active")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'email2',
            'username',
            'password'
        ]

    def clean_email2(self):

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails do not match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")

        return email

class EmployerAddForm(forms.Form):

    # to take the input of company name
    company_name = forms.CharField()
    # to take the input of the company email
    email = forms.EmailField(label='Email address')

class ExpenseAddForm(forms.Form):

    company_name = forms.ModelChoiceField(queryset=Employer.objects.all())

    # to take the input of shift date
    shift_date = forms.DateField()
    # the pay/rate for the shift /hr
    pay_rate = forms.FloatField(required=False)
    #total hours
    total_hours = forms.FloatField(required=False)
    # any adidtional costs outside of the rate
    additional_cost = forms.FloatField(required=False)
    #notes or desciptions
    description = forms.CharField(max_length=200, required=False)



