from django.urls import path, include
from Recruiter import views
app_name="Recruiter"

urlpatterns = [
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Job/',views.Job,name='Job'),
    path('deljob/<int:id>',views.deljob,name='deljob'),
    path('editjob/<int:id>',views.editjob,name='editjob'),
    path('Viewrequest/',views.Viewrequest,name='Viewrequest'),
    path('acceptu/<int:id>',views.acceptu,name='acceptu'),
    path('rejectu/<int:id>',views.rejectu,name='rejectu'),
]