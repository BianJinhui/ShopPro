import hashlib

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,HttpResponse
from Store.models import User
from Store.forms import UserForm

def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

def index(request):
    return HttpResponse("hello world")

def register(request):
    if request.method == "POST":
        valid_data = UserForm(request.POST)
        if valid_data.is_valid():
            username = valid_data.cleaned_data.get("username")
            password = valid_data.cleaned_data.get("password")
            user = User()
            user.username = username
            user.password = set_password(password)
            user.save()
            return HttpResponseRedirect("/Store/login/")
    return render(request,"register.html")

def login(request):
    errors = ""
    if request.method == "POST":
        valid_data = request.POST
        username = valid_data.get("username")
        password = valid_data.get("password")
        user = User.objects.filter(username = username).first()
        if user:
            db_password = user.password
            if set_password(password) == db_password:
                response = HttpResponseRedirect("/Store/index/")
                response.set_cookie("username",username)
                request.session["username"] = username
                return response
    return render(request,"login.html",locals())


# Create your views here.
