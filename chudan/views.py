from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chudan.models import *
from django.db.models import Q


# Create your views here.
def home(request):
	return render(request, 'attendance/home.html')

@csrf_exempt
def signin(request):
    #probar
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('mark')
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            return redirect('home')
    else:
        # Return an 'invalid login' error message.
        return redirect('home')

def signout(request):
    logout(request)
    return redirect('home') #home

def mark(request):
    if request.user.is_authenticated():
        return render(request, 'attendance/mark.html')
    else:
        return redirect('home') #home

@csrf_exempt
def do_mark(request):
    if not request.user.is_authenticated():
        return redirect('home') #home

    user_id = request.POST.get('user_id')
    date = request.POST.get('date')

    if user_id:
        try:
            Attendance.objects.get(user_id=user_id,timestamp=date)
        except:
            #create attendance
            att = Attendance(user_id=user_id,timestamp=date)
            att.save()

    #get all attendances
    attendances = Attendance.objects.filter(timestamp=date)

    return render(request, 'attendance/do_mark.html',{"attendances":attendances})

@csrf_exempt
def names(request):
    term = request.POST.get("term")
    response_data = []

    results = User.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))

    for r in results:
        element = {}
        element['id'] = r.id
        element['label'] = r.first_name + " " + r.last_name
        element['value'] = r.first_name + " " + r.last_name
        response_data.append(element)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def kenshi(request):
    if request.user.is_authenticated():
        return render(request, 'attendance/kenshi.html')
    else:
        return redirect('home') #home

@csrf_exempt
def new_kenshi(request):
    pass