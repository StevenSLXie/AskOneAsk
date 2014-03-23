from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from lists.models import Qns,Ans,Person
from random import randint
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django_tables2 import RequestConfig
from lists.tables import QnsTable,AnsTable,UserTable

# Create your views here.

flag = False
sampleNum = 1


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
    else:
        return render(request,'login.html')
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            if not request.POST.get('remember_me',None):
                request.session.set_expiry(0)
            p = Person.objects.get(user=user)
            if p.city == 'Earth':
                return redirect('/more')
            else:
                return redirect('/')
			#return redirect('/more')
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def new_ask(request):
    render(request,'ask.html')
    if request.POST.get('qns_text'):
        if request.POST['qns_text'] != '':
            Qns.objects.create(qns=request.POST['qns_text'],author=request.user)
        return redirect('/answer')
    elif request.POST.get('backToMenu'):
        return redirect('/')
    else:
        return render(request,'ask.html')

def new_answer(request):
    num = Qns.objects.count()
	#flag = False
    global flag
    global sampleNum
    if not flag:
        sampleNum = randint(1,num)
        flag = True
    sample = Qns.objects.get(id=sampleNum)
    para = {'Question':sample.qns,'Author':sample.author}
    if request.POST.get('ans_text'):
        if request.POST['ans_text'] != '':
            Ans.objects.create(answer=request.POST['ans_text'],person=request.user,qns=sample)
        flag = False
        return redirect('/ask')
    elif request.POST.get('backToMenu'):
        return redirect('/')
    else:
        return render(request,'answer.html',para)


def signup(request):
    if request.method == 'POST':
        if 'i_have_an_account' in request.POST:
            return redirect('/login')
        elif (not request.POST['username']) or (not request.POST['password']) or (not request.POST['password2']) or (not request.POST['email']):
            return render(request,'signup.html')
        elif request.POST['password'] != request.POST['password2']:
            return render(request,'signup.html')
		#if 'i_have_an_account' not in request.POST:	
        User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        curUser = User.objects.get(username=request.POST['username'])
        Person.objects.create(user=curUser)
        return redirect('/login')
    else:
        return render(request,'signup.html')

def user_info_input(request):
    if request.method == 'POST':
        if request.POST.get('later'):
            return redirect('/')
        else:
			#request.user.city = request.POST['city']
            if not request.POST.get('status',None):
                temp_state = True
            else:
                temp_state = False
            curPer = Person.objects.get(user=request.user)
            curPer.city = request.POST['city']
            curPer.status = temp_state
            curPer.save()
			#Person.objects.create(user=request.user,city=request.POST['city'],status=temp_state)
            return redirect('/')
    else:
	    return render(request,'user_information_input.html')
        

def print_qns_by_asker(request):
    table = QnsTable(Ans.objects.filter(qns__author=request.user))
    RequestConfig(request).configure(table)
    return render(request, 'print_answer.html', {'table': table})

def print_answer_by_answerer(request):
    table = AnsTable(Ans.objects.filter(person=request.user))
    RequestConfig(request).configure(table)
    return render(request,'print_answer.html',{'table':table})

def home(request):
    return render(request,'home.html')

def print_people_detail(request,curUser):
    table = UserTable(Person.objects.filter(user__username=curUser))
    RequestConfig(request).configure(table)
    return render(request,'user_profile.html',{'table':table})
	#return redirect('/ask')

def logout(request):
    auth_logout(request)
    return redirect('/login')
