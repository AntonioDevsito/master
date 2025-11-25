from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.
""" def home(request):
    return HttpResponse("<h1>WOrks</h1>") """

def home(request):
    today = date.today()
    stack = [{'id':"python",'name':"python"} ,{'id':"Django",'name':"Django"},{'id':"Golang",'name':"Golang"},{'id':"PHP",'name':"PHP"},{'id':"JS",'name':"JS"}]
    return render(request,"landing/landing.html",{
        "name":"Fernando",
        "edad":15,
        "today":today,
        "stack":stack
    })
def stack_detail(request,tool):
    return HttpResponse(f"tecnologia:{tool}")
    