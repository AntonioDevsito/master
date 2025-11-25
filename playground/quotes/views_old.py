from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
#import traceback
# Create your views here.

def days_of_week(request,day):
    
    quotes_text = None
    frase = {
        "monday":"frase del dia lunes: 'el exito es la suma de pequeños esfuerzos'",
        "tuesday":"frase del martes:  'la perseverancia es parte del exito' ",
        "wednesday":"frase del miercoles: 'si no luchas por lo que quieres no lo mereces'",
        "thursday":"frase del jueves: 'una accion dice mas que mil palabras'",
        "friday":"frase del viernes: 'caminando en linea recta no puedes llegar muy lejos'",
        "saturday":"frase del sabado: 'Que sean pasos pequeños no significa que no avanzes'",
        "sunday":"frase del domingo: 'El no intentarlo no conseguiras saber si te gusta algo'"
    }
    dias =tuple(frase.keys())
    try:
     quotes_text = days_of_week(day)

     if isinstance(day,str):
        quotes_text=frase[day]
     elif isinstance(day,int):
        day_num=int(day)
        quotes_text= frase[dias[day_num-1]]
        return HttpResponse(quotes_text)
    except IndexError:
            return HttpResponseNotFound("frase no encontrada")
    except TypeError:        
        return HttpResponseNotFound("frase no encontrada")
    except Exception as e:
        error_type = type(e).__name__#nombre del tipo de error
        return HttpResponseNotFound(f"frase no encontrada/error {error_type}-{e}")
    except KeyError:
        render(request, '404.html')
    

        

