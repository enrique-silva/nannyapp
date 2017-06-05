from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import render, redirect
from .models import User, Employer, Expense, Invoice
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm, EmployerAddForm, ExpenseAddForm, InvoiceAddForm
from .filters import ExpenseFilter



# homepage
def home_page(request):
    return render(request, 'polls/home_page.html')


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/home_page_user")
    return render(request, 'polls/form.html', {"form": form, "title": title})


def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        # return something at some point
        return redirect("/home_page_user")

    return render(request, 'polls/form.html', {"form": form, "title": title})


def logout_view(request):
    logout(request)
    return redirect("/home_page")


def expense_add(request):
    title = "Add Expense"

    form = ExpenseAddForm(request.POST)
    print('TEST')
    if form.is_valid():
        company = form.cleaned_data.get('company', '')
        # company_name_not_primary = form.cleaned_data.get('company_name','')
        # b = Employer.objects.get(company_name=company_name_not_primary)
        # company_name = b.id
        # print('TEST',company)
        pay_rate = form.cleaned_data.get('pay_rate', '')
        additional_cost = form.cleaned_data.get('additional_cost', '')
        shift_date = form.cleaned_data.get('shift_date', '')
        total_hours = form.cleaned_data.get('total_hours', '')
        description = form.cleaned_data.get('description', '')

        # return something at some point
        expense_obj = Expense(company=company, pay_rate=pay_rate,
                              additional_cost=additional_cost, shift_date=shift_date,
                              total_hours=total_hours, description=description, )
        expense_obj.save()
        return redirect("/showdata")
    else:
        form = ExpenseAddForm()
        return render(request, 'polls/form.html', {"form": form, "title": title})


def invoice_add_view(request):
    expense_list = Expense.objects.all()
    expense_filter = ExpenseFilter(request.GET, queryset=expense_list)
    return render(request, 'polls/expense_list.html', {'filter': expense_filter})


    #title = "Add invoice"

    # form = InvoiceAddForm(request.POST)
    #
    # if form.is_valid():
    #     c_name = form.cleaned_data.get('c_name')
    #     start_date = form.cleaned_data.get('start_date', '')
    #     end_date = form.cleaned_data.get('end_date', '')
    #     # return something at some point
    #     invoice_obj = Invoice(c_name=c_name, start_date=start_date, end_date=end_date)
    #
    #     return redirect("/showdata")
    # else:
    #     form = InvoiceAddForm()
    #     return render(request, 'polls/form.html', {"form": form, "title": title})



def employer_add_view(request):
    title = "Add Employer"

    form = EmployerAddForm(request.POST)
    if form.is_valid():
        company_name = form.cleaned_data.get('company_name', '')
        email = form.cleaned_data.get('email', '')
        # return something at some point
        employer_obj = Employer(company_name=company_name, email_address=email)
        employer_obj.save()
        return redirect("/showdata")
    else:
        form = EmployerAddForm()
        return render(request, 'polls/form.html', {"form": form, "title": title})





# the function executes with the signup url to take the inputs
# def signup(request):
#     if request.method == 'POST':  # if the form has been filled
#
#         form = UserForm(request.POST)
#
#         if form.is_valid():  # All the data is valid
#             user_name = request.POST.get('user_name', '')
#             password = request.POST.get('password', '')
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#         # creating an user object containing all the data
#         user_obj = User(user_name=user_name, password=password, first_name=first_name, last_name=last_name)
#         # saving all the data in the current object into the database
#         user_obj.save()
#
#         return HttpResponseRedirect('/home_page_user')
#         # render(request, 'polls/signup.html') # Redirect after POST
#     # {'user_obj': user_obj,'is_registered':True }
#     else:
#         form = UserForm()  # an unboundform
#
#         return render(request, 'polls/signup.html', {'form': form})


def home_page_user(request):
    return render(request, 'polls/home_page_user.html')
    # the function executes with the showdata url to display the list of registered users


def showdata(request):
    all_users = User.objects.all()
    employer = Employer.objects.all()
    expense = Expense.objects.all()
    invoice = Invoice.objects.all()
    return render(request, 'polls/showdata.html', {'all_users': all_users, 'employer': employer,
                                                   'expense': expense, 'invoice':invoice})
