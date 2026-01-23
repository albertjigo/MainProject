
from django.urls import path, include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('Recruiterregistration/',views.Recruiterregistration,name='Recruiterregistration'),
    path('Login/',views.Login,name='Login'),
    path('index/',views.index,name='index'),

    
]