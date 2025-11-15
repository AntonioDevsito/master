from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
days_of_week = {
    "monday": "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "tuesday": "No cuentes los días, haz que los días cuenten.",
    "wednesday": "La única manera de hacer un gran trabajo es amar lo que haces.",
    "thursday": "El fracaso es simplemente la oportunidad de comenzar de nuevo, esta vez de forma más inteligente.",
    "friday": "La vida es 10% lo que me ocurre y 90% cómo reacciono a ello.",
    "saturday": "No esperes. El tiempo nunca será justo.",
    "sunday": "Cree que puedes y ya estás a mitad de camino."
}        
def days_week_with_number(request, day):  
   days= list(days_of_week.keys())
   if day > len(days):
       return HttpResponseNotFound("el dia no existe")
   redirect_day = days[day-1]
   redirect_path = reverse("day-quote",args=(redirect_day))
   #return HttpResponseRedirect(f"/quotes/{redirect_day}")
   return HttpResponseRedirect(f"{redirect_path}")
def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    
    except:
        return HttpResponseNotFound("Frase no encontrada para el día especificado.")
def index(request):
    list_items=""
    days = list(days_of_week.keys())
    for day in days:
        day_path = reverse("day-quote",args=[day,])
        list_items+=f'<li><a href="{day_path}">{day.capitalize()}</a></li>'
    response_html=f"<ul>{list_items}</ul"
    return HttpResponse(response_html)