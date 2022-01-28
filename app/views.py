from django.contrib.auth import authenticate, login, logout, forms
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required


    
def home(request):
    if not request.user.is_authenticated:
        if request.POST:
            if 'signup_btn' in request.POST:
                form = UserForm(request.POST)
                if form.is_valid():
                    user = form.cleaned_data['username']
                    passs = form.cleaned_data['password1']
                    form.save()
                    auth = authenticate(username=user, password=passs)
                    if auth:
                        login(request, auth)
                return HttpResponseRedirect('feeds/')
            if 'login_btn' in request.POST:
                form = forms.AuthenticationForm(request=request, data=request.POST)
                if form.is_valid():
                    user = form.cleaned_data['username']
                    passs = form.cleaned_data['password']
                    auth = authenticate(username=user, password=passs)
                    if auth:
                        login(request, auth)
                else:
                    messages.error(request, "Please Type Correct Username and Password")
                    return HttpResponseRedirect('feeds/')
                    
                return HttpResponseRedirect('feeds/')
        else:
            return render(request, 'app/register.html')
    else:
        return HttpResponseRedirect('feeds/')
  
  
@login_required(login_url='/')
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')


def check_username(request, user=None):
    data = user
    if data is not None:
        if len(data) >= 5:
            try:
                obj = User.objects.filter(username=data)
            except:
                obj = None
            if obj:
                return JsonResponse({'status':0})
            else:
                return JsonResponse({"status":1})
        else:
            return JsonResponse({"status":2})
    else:
        return JsonResponse({'status':3})


@login_required(login_url='/')
def feed(request):
    context = {}
    context['name'] = "deepak"
    obj = User.objects.get(id=request.user.id)
    follow = User.objects.exclude(id__in=[request.user.id]+[i.id for i in obj.following.all()])
    not_follow = User.objects.filter(id__in=[i.id for i in obj.following.all()])
    status = Status.objects.filter(created_by__in=[request.user.id]+[i.id for i in obj.following.all()])
    context['data'] = obj
    context['status'] = status
    context['follow'] = follow
    context['not_follow'] = not_follow
    if request.session.get('message') is None:
        messages.success(request, "Hiii WElcome Mr. {}".format(request.user.username))
        request.session['message'] = "YES"
    return render(request, 'app/feeds.html', context)
    
    
@login_required(login_url='/')
def follow(request, id=None):
    try:
        user = User.objects.get(id=id)
    except:
        raise Http404
    obj = User.objects.get(id=request.user.id)
    obj.following.add(user)
    user.followed_by.add(obj)
    messages.success(request, "You are Now Following {}".format(user.username))
    return HttpResponseRedirect('/feeds/')
    
    
@login_required(login_url='/')
def unfollow(request, id=None):
    try:
        user = User.objects.get(id=id)
    except:
        raise Http404
    obj = User.objects.get(id=request.user.id)
    obj.following.remove(user)
    user.followed_by.remove(obj)
    messages.success(request, "You have Un-Followed {}".format(user.username))
    return HttpResponseRedirect('/feeds/')
    


@login_required(login_url='/')
def post_status(request):
    if request.POST:
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have Posted a new status Update!!")
            
        return HttpResponseRedirect('/feeds/')
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def update_profile(request):
    context = {}
    obj = User.objects.get(id=request.user.id)
    
    if request.POST:
        data=request.POST
        try:
            obj.first_name=data.get('first_name')
            obj.last_name=data.get('last_name')
            obj.birth_date=data.get('bith_date')
            obj.profile_pic=request.FILES.get('profile_pic')
            obj.save()
            messages.success(request, "Profile Updated SuccessFully!!")
            return HttpResponseRedirect('/feeds/')
        except:
            messages.error(request, "There is Some error Please Try Again!")
            return HttpResponseRedirect('/update/')
    context['form'] = UserForm(data=obj)
    
    return render(request, 'app/update_profile.html', context)
    
    