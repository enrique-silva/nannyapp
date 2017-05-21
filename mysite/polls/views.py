from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import render, redirect
from polls.models import User
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm, UserRegisterForm


# homepage
def home_page(request):
    return render(request, 'polls/home_page.html')

def login_view(request):

    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request, user)
        return redirect("/home_page_user")
    return render(request, 'polls/form.html', {"form":form,"title":title})



def register_view(request):

    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username,password=password)
        login(request, new_user)
        #return something at some point
        return redirect("/home_page_user")

    return render(request, 'polls/form.html',{"form":form,"title":title})

def logout_view(request):
    logout(request)
    return redirect("/home_page")













#the function executes with the signup url to take the inputs
def signup(request):
    if request.method == 'POST':  # if the form has been filled

        form = UserForm(request.POST)

        if form.is_valid():  # All the data is valid
            user_name = request.POST.get('user_name', '')
            password = request.POST.get('password', '')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
        # creating an user object containing all the data
        user_obj = User(user_name=user_name, password=password, first_name=first_name, last_name=last_name)
        # saving all the data in the current object into the database
        user_obj.save()

        return HttpResponseRedirect('/home_page_user')
        # render(request, 'polls/signup.html') # Redirect after POST
    # {'user_obj': user_obj,'is_registered':True }
    else:
        form = UserForm()  # an unboundform

        return render(request, 'polls/signup.html', {'form': form})


def home_page_user(request):
    return render(request, 'polls/home_page_user.html')
    # the function executes with the showdata url to display the list of registered users


def showdata(request):
    all_users = User.objects.all()
    return render(request, 'polls/showdata.html', {'all_users': all_users,})

