from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def feedback(request):
    return HttpResponse("Thank You")
def contactprocess(request):
    a= request.POST['txt1']
    b= request.POST['txt2']
    c= int(a) + int(b)
    ans = "sum is" + str(c)
    return HttpResponse(ans)