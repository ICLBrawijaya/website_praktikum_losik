from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Ini buat nampilin halaman login
def loginpage(request):
    return render(request,'loginpage.html')

# Ini buat ngelakuin proses login
def performlogin(request):
    # Kalau misal fungsi ini diakses langsung via url maka error
    if request.method != 'POST':
        return HttpResponse("Method not allowed")
    else:
        username = request.POST['username']
        password = request.POST['password']
        # ini buat ngematch in antara username sama password yg di input lewat form apakah cocok dengan database username password yang udah ada
        userobj = authenticate(request,username=username, password=password)
        # Kalau misal username dan password ga match maka value userobj = None . kalau cocok value userobj = namauser
        if userobj is not None :
            auth_login(request,userobj)
            # Ini buat ngirim messages
            messages.success(request,'Login Berhasil')
            return redirect('index')
        else:
            messages.error(request,'Username atau Password Salah')
            return redirect('loginpage')

# ini namanya dekorator. Kalau mau akses fungsi ini user harus udah login. kalau belum login gabisa
@login_required
def index(request):
    return render(request,'index.html')

# digunakan untuk logout dari akun yang sudah terlogin
@login_required
def performlogout(request):
    auth_logout(request)
    return redirect(loginpage)
