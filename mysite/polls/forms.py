from django import forms
from .models import Employer, Expense, Invoice
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.widgets import AdminDateWidget

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
                raise forms.ValidationError("This user or password is incorrect")

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
    Title = 'Add an Employer'
    # to take the input of company name
    company_name = forms.CharField()
    # to take the input of the company email
    email = forms.EmailField(label='Email address')


class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseAddForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['company', 'shift_date']
        widgets = {
            'shift_date': DateInput(),
        }

    pay_rate = forms.FloatField()
    total_hours = forms.FloatField()
    additional_cost = forms.FloatField()
    description = forms.CharField()


class InvoiceAddForm(forms.ModelForm):
    # to take the input of company name

    class Meta:
        model = Invoice
        fields = ['c_name','start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
