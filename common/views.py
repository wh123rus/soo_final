from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm


# register 함수에 접근할 때 로그인 필요하도록 설정
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None and user.is_authenticated:
                login(request, user)
            return redirect('common:done')
						# login() 함수 호출 전에 로그인되어있는지 확인
    else:
        form = UserForm()
        return render(request, 'common/register.html', {'form': form})

def done(request):
    return render(request, 'common/done.html')

def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('common:password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/password_change.html', {'form':form})

def password_change_done(request):
    return render(request, 'common/password_change_done.html')
