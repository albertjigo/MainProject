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
    # path('Viewexamination/',views.Viewexamination,name='Viewexamination'),
    # path('Viewquestion/<int:id>',views.Viewquestion,name='Viewquestion'),

    path('viewexam/',views.viewexam,name='viewexam'),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('ajaxexamanswer/',views.ajaxexamanswer,name='ajaxexamanswer'),
    path('ajaxtimer/',views.ajaxtimer,name='ajaxtimer'),
    path('successer/',views.successer,name='successer'),

    path('logout/',views.logout,name='logout'),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('Notification/',views.Notification,name="Notification"),
  
]