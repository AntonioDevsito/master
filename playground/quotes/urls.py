from django.urls import path
from . import views
from . import views_old

urlpatterns = [
    #path("",views.index,name="index"),
    path('days/', views.days, name="days"),
    path("dias/<str:day>",views.days_detail,name="day"),
    path("days_week/<int:day>/", views_old.days_of_week,name="days_week_with_number"),
    path("days_of_week/<str:day>/", views_old.days_of_week,name="day-quote"),
    
]