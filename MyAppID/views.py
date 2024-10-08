from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.success(request,"Password does not match")

    context={'form':form}
    return render(request,'register.html',context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.success(request,"Username or Password incorrect")

    context={}
    return render(request,'login.html',context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')