from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
def my_login(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['用户名'], password = request.POST['密码'] )
        if user is None:
            return render(request, 'login.html', {'error': '用户名或密码错误!'})
        else:
            login(request,user)
            return redirect('home')
    else:
        return render(request, 'login.html')
def my_logout(request):
    logout(request)
    return redirect('home')
def my_register(request):
    if request.method == 'POST':
        my_form = UserCreationForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            user = authenticate(username=my_form.cleaned_data['username'], password=my_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        my_form = UserCreationForm()
    content = {'my_form': my_form}
    return render(request, 'register.html', content)
