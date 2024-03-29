from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from account.forms import Payment_Form, Profile_Form, myuser_form, ChangePassword
from account.models import Payment
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return HttpResponseRedirect(reverse('showtime_list'))
        else:
            context={
                'username':username,
                'error':"cant find"+" "+username
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('showtime_list'))
        context={}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def profile_details(request):
    profile=request.user.profile
    context={
        'profile':profile
    }
    return render(request,'accounts/profile_details.html',context)

@login_required
def payment_list(request):
    payments=Payment.objects.filter(myprofile=request.user.profile).order_by('-transaction_time')
    context={
        'payments':payments
    }
    return render(request,'accounts/payment_list.html',context)

@login_required
def payment_creat(request):
    if request.method=="POST":
        payment_form=Payment_Form(request.POST)
        if payment_form.is_valid():
            payment=payment_form.save(commit=False)
            payment.myprofile=request.user.profile
            payment.save()
            request.user.profile.deposit(payment.amount)
            return HttpResponseRedirect(reverse('payment_list'))
    else:
        payment_form=Payment_Form()
    context={
        'payment_form':payment_form
    }
    return render(request,"accounts/payment_creat.html",context)

@login_required
def profile_edit(request):
    if request.method=="POST":
        profile_form=Profile_Form(request.POST,files=request.FILES,instance=request.user.profile)
        user_edit=myuser_form(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            user_edit.save()
            return HttpResponseRedirect(reverse('profile_details'))
    else:
        profile_form=Profile_Form(instance=request.user.profile)
        user_edit = myuser_form( instance=request.user)
    context={
        'profile_form':profile_form,
        'user_edit':user_edit
    }
    return render(request,"accounts/profile_edit.html",context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        print("data post:", request.POST['password'])
        if form.is_valid():
            new_pass = request.POST['password']
            user=User.objects.get(id=request.user.id)
            print("user:",user)
            user.set_password(new_pass)
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = ChangePassword()
    context={
        'form':form
    }
    return render(request, "accounts/password_change.html", context)


