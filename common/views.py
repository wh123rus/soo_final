from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm

# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#         return redirect('common:done')
#     else:
#         form = UserForm()
#     return render(request, 'common/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('common:done')
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
