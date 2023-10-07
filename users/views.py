from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, "Senhas não conferem.")
            return redirect('/users/register')
        
        if len(password) < 6:
            messages.add_message(request, constants.ERROR, "A senha deve possuir mais de 6 caracteres.")
            return redirect('/users/register')
        
        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso")            
        except:
            messages.add_message(request, constants.ERROR, "Erro externo do sistema, contate um administrador.")
            return redirect('/users/register')
        
        return redirect('/users/register')
        