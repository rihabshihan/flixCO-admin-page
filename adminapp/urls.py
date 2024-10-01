from django.contrib import admin
from django.urls import path
from adminapp import views

urlpatterns = [
    path("",views.login,name="login"),
    path("forgotpass/",views.forgotpass,name="forgotpass"),
    path("newpass/",views.newpass,name="newpass"),
    
    path("homepage/",views.homepage,name="homepage"),
    path("editmovie/",views.editmovie,name="editmovie"),
    path("createmovie/",views.createmovie,name="createmovie"),
    path("viewmovie/",views.viewmovie,name="viewmovie"),
    path("userhome/",views.userhome,name="userhome"),
    path("subscription/",views.subs,name="subs"),
    path("viewplan/",views.viewplan,name="viewplan"),
    path("createplan/",views.createplan,name="createplan"),
    path("reports/",views.reports,name="reports"),
    path("chnagepass/",views.changepass,name="changepass"),
    
    
]
