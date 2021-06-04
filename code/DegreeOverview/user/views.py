from threading import local
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Account, Student, CourseDesigner, NonCourseDesigner
from django.contrib import messages
import datetime

# Create your views here.


def login(request):
    if request.method == 'GET':
        # get the login page
        return render(request, 'login.html')
    elif request.method == 'POST':
        # data processing
        username = request.POST['username']
        password = request.POST['password']

        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            messages.error(request, 'username or password is error')
            print('---login user error %s' % (e))
            return HttpResponseRedirect('login')

        # check password
        if password != account.password:
            messages.error(request, 'username or password is error')
            return HttpResponseRedirect('login')
        else:
            type = account.type
            # record session
            request.session['username'] = username
            request.session['uid'] = account.id
            request.session['utype'] = type
            # set cookie, and expiration time is 3h
            # resp = HttpResponse('---Login Successful---')
            # resp.set_cookie('uid', account.id, 3600*3)
            # resp.set_cookie('username', username, 3600*3)
            # resp.set_cookie('utype', type, 3600*3)

            utype = request.session.get('utype', 'none')
            print(utype)
            if(type == 'NonCourseDesigner'):
                return HttpResponseRedirect('ncdMain')
            elif(type == 'CourseDesigner'):
                return HttpResponseRedirect('cdMain')
            else:
                return HttpResponseRedirect('stuMain')


def logout(request):
    # delete all cookies and sessions
    request.session.flush()
    utype = request.session.get('utype', 'none')
    print(utype)
    return HttpResponseRedirect('login')


def cdMain(request):
    if(request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('login')
    else:
        currentYear = datetime.datetime.now().year
        years = range(currentYear, 2004, -1)
        return render(request, 'cdMain.html', locals())


def ncdMain(request):
    if(request.session.get('utype', 'none') != 'NonCourseDesigner'):
        return HttpResponseRedirect('login')
    else:
        currentYear = datetime.datetime.now().year
        years = range(currentYear, 2004, -1)
        return render(request, 'ncdMain.html', locals())


def stuMain(request):
    if(request.session.get('utype', 'none') != 'Student'):
        return HttpResponseRedirect('login')
    else:
        currentYear = datetime.datetime.now().year
        years = range(currentYear, 2004, -1)
        return render(request, 'stuMain.html', locals())


def home(request):
    if(request.session.get('utype', 'none') == 'none'):
        return HttpResponseRedirect('login')
    else:
        utype = request.session.get('utype', 'none')
        print(utype)
        if(utype == 'NonCourseDesigner'):
            return HttpResponseRedirect('ncdMain')
        elif(utype == 'CourseDesigner'):
            return HttpResponseRedirect('cdMain')
        else:
            return HttpResponseRedirect('stuMain')
