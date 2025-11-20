from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 

    
def days(request):
    days_list=[
        {"id":"monday","name":"monday","frase":"El éxito es la suma de pequeños esfuerzos repetidos día tras día."},
        {"id":"tuesday","name":"tuesday","frase":"No cuentes los días, haz que los días cuenten."},
        {"id":"wednesday","name":"wednesday","frase":"La única manera de hacer un gran trabajo es amar lo que haces."},
        {"id":"thursday","name":"thursday","frase":"El fracaso es simplemente la oportunidad de comenzar de nuevo, esta vez de forma más inteligente."},
        {"id":"friday","name":"friday","frase":"La vida es 10% lo que me ocurre y 90% cómo reacciono a ello."},
        {"id":"saturday","name":"saturday","frase":"No esperes. El tiempo nunca será justo."},
        {"id":"sunday","name":"sunday","frase": "Cree que puedes y ya estás a mitad de camino."},
    ]
    return render(request,"html/days.html",{
        "list":days_list,
    })

def days_detail(request,day):
    return HttpResponse(f"Frase del dia: {day}")
    