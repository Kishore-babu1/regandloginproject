from django.shortcuts import render
from django.views import View
from .forms import RegModelForm,LoginForm
from .models import RegModel
from django.http import HttpResponse
# Create your views here.
class RegInput(View):
    def get(self, request):
        con_dic = {"regform": RegModelForm()}
        return render(request, 'reginput.html', con_dic)
class Reg(View):
    def post(self, request):
        rf = RegModelForm(request.POST)
        if rf.is_valid():
            rf.save()
            return HttpResponse("Registration successfull")
class LoginInput(View):
    def get(self, request):
        con_dic = {"loginform": LoginForm()}
        return render(request, "logininput.html", con_dic)
class Login(View):
    def post(self, request):
        lf = LoginForm(request.POST)
        if lf.is_valid():
            user = RegModel.objects.filter(username=lf.cleaned_data["username"],
                                           password=lf.cleaned_data["password"])
            if not user:
                return HttpResponse("invalid username or password")
            else:
                return HttpResponse("login successfull")

