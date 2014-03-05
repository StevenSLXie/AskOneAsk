from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Qns,Ans
from random import randint
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_tables2 import RequestConfig
from lists.tables import QnsTable,AnsTable

# Create your views here.

flag = False
sampleNum = 1

'''
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return render(request,'home.html')
        else:
            return redirect('/')
    else:
        return redirect('/')
'''
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
        if 'i_have_an_account' not in request.POST:	
            User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        return redirect('/login')
    else:
        return render(request,'signup.html')

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

def people_detail(request):
    return redirect('/')
