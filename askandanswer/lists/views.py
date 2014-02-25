from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Qns,Ans
from random import randint
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_tables2 import RequestConfig
from lists.tables import QnsTable

# Create your views here.

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
    if request.method == 'POST':
        Qns.objects.create(qns=request.POST['qns_text'],author=request.user)
        return redirect('/answer')
    else:
        return render(request,'home.html')

def new_answer(request):
    num = Qns.objects.count()
    sampleNum = randint(1,num)
    sample = Qns.objects.get(id=sampleNum)
    para = {'Question':sample.qns,'Author':sample.author}
    render(request,'qns.html',para)
    if request.method == 'POST':
        sample.answerSet.add(Ans.objects.create(answer=request.POST['ans_text'],person=request.user))        
        return redirect('/ask')
    else:
        return render(request,'qns.html',para)

def signup(request):
    if request.method == 'POST':
        if 'i_have_an_account' not in request.POST:	
            User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        return redirect('/login')
    else:
        return render(request,'signup.html')

def print_answers(request):
    table = QnsTable(Qns.objects.filter(author=request.user))
    RequestConfig(request).configure(table)
    return render(request, 'print_answer.html', {'table': table})
