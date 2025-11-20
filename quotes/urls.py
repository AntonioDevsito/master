from django.urls import path
from . import views
urlpatterns = [
    #path("",views.index,name="index"),
    path('days/', views.days, name="days"),
    path("dias/<str:day>",views.days_detail,name="day"),
    #path("<int:day>/", views.days_week_with_number,name="days_week_with_number"),
    #path("<str:day>/", views.days_week,name="day-quote"),
    
]