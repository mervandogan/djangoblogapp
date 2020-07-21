from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout            #bu modül databesa bakıp kullanıcımızın olup olmadığımı kontrol eder(authenticate)

# Create your views here.

def register(request):

    form=RegisterForm(request.POST or None)        #requestimizin post mu getmi olduğunu ayarlamıyorum eğer post değilse null devreye giriryor ve aynı aşşağıdaki gibi boş request oluyor.
    
    if form.is_valid():                   #forms dan clean methodunu çağırır yani parolalar eşleşiyormu eşleşmiyormu kısmı.

        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)                     #Bu Userımız hem kayıt olmuş oldu hemde otomatik olarak bu login sayesinde sisteme giriş yapmış oldu     
        messages.success(request,"Başarıyla Kayıt Oldunuz")
        return redirect("index")
    context={                                       #üstdeki koşulu geçemediğimiz zamana hata kısmını bu bölümde alıyoruz parolanız uyuşmuyor gibi
        "form": form

        }
    return render(request,"register.html",context)
    


   


 

def loginUser(request):
    form=LoginForm(request.POST or None)

    context={
        "form": form
    }

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)         #database bakıcak öyle bir kullanıcımız varsa bize bu kullanıcıyı getiricek

        if user is None:  #öyle bir userimiz yoksa
            messages.warning(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)      #kullanıcıya giriş yapmasını imkan verdik
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)

    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")