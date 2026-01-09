from django.urls import path, include
from User import views
app_name="User"

urlpatterns = [
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('Viewjob/',views.Viewjob,name='Viewjob'),
    path('Viewmore/<int:id>',views.Viewmore,name='Viewmore'),
    path('Notes/',views.Notes,name='Notes'),
    path('notedel/<int:id>',views.notedel,name='notedel'),
    path('Viewnotes/',views.Viewnotes,name='Viewnotes'),
    path('Upload/<int:id>',views.Upload,name='Upload'),
    path('Myrequest/',views.Myrequest,name='Myrequest'),
    path('delf/<int:id>',views.delf,name='delf'),
    path('Viewexamination/',views.Viewexamination,name='Viewexamination'),
    path('Viewquestion/<int:id>',views.Viewquestion,name='Viewquestion'),

]