from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def forgotpass(request):
    return render(request, "fg-pass.html")

def newpass(request):
    return render(request, "new-pass.html")



#home page
def homepage(request):
    return render(request, "home-page.html")

#edit movie
def editmovie(request):
    return render(request, "edit-movie.html")

def createmovie(request):
    return render(request, "create-movie.html")

def viewmovie(request):
    return render(request, "view-movie.html")

#User-homepage
def userhome(request):
    return render(request, "user-home.html")

def subs(request):
    return render(request, "subs.html")

def viewplan(request):
    return render(request, "view-plan.html")

def createplan(request):
    return render(request, "create-plan.html")

def reports(request):
    return render(request, "reports.html")

def changepass(request):
    return render(request, "change-pass.html")




