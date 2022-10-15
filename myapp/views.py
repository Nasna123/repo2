from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fun1(request):
    return HttpResponse("SUCCESFULLY CREATED HTTP PAGE")

def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')        
