from ast import Param
from pyexpat import model
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import pickle




# Create your views here.
# def index(request):        
#     return render(request,'test/index.html')

def home(request):
    return render(request,'test/index.html')

def process_presection(request):
    sourceapp = request.POST.get('sourceapp')
    remoteapp = request.POST.get('remoteapp')
    remotecpprot = request.POST.get('remotecpprot')
    tcpexchange = request.POST.get('tcpexchange')
    remoteip = request.POST.get('remoteip')
    rmotebyte = request.POST.get('rmotebyte')
    model1 = pickle.load(open('model1.pkl','rb'))
    lis = []
    lis.append(remoteapp)   
    lis.append(sourceapp)   
    lis.append(remotecpprot)   
    lis.append(tcpexchange)   
    lis.append(remoteip)  
    lis.append(rmotebyte) 
    print(lis)
    ans = model1.predict([lis]) 
    if ans == 0:
        ans="It is safe domain"
    elif ans ==1:
        ans="it is malicious domain"
    else:
        ans="No t predict for domain"
    pram={'sourceapp': sourceapp,'remotecpprot':remotecpprot, 'remoteapp':remoteapp,'tcpexchange':tcpexchange,'remoteip':remoteip,'rmotebyte':rmotebyte,'ans':ans}
    return render(request,'test/result.html', pram)
        