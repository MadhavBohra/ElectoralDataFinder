from django.urls import path
#My Code 
from myapp import views


urlpatterns = [
    path("",views.index,name='home'),
    path('ajax/load-districts',views.load_districts,name='ajax_load_districts'),
    path('ajax/load-acs',views.load_acs,name='ajax_load_acs')
]