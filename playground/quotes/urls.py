from django.urls import path
from . import views


urlpatterns = [
    #path("",views.index,name="index"),
    path('days/', views.days, name="days"),
    path("dias/<str:day>",views.days_detail,name="day"),

]