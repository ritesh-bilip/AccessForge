from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm , LoginForm

# Create your views here.

def signup(request):
  if request.method=='POST':
    form=SignUpForm(request.POST)
    if form.is_valid():
      user=form.save()
      user = authenticate(request, email=user.email, password=form.cleaned_data['password'])
      login(request,user)
      messages.success(request,"Account create succesfully")
      return redirect('home')
    else:
            # 🔥 This was missing: return the form with errors
            return render(request, 'signup.html', {'form': form})
  else:
    form=SignUpForm()
    return render(request,'signup.html',{'form':form})
def login_user(request):
  if request.method=='POST':
    form= LoginForm(request.POST)
    if form.is_valid():
      email=form.cleaned_data['email']
      password=form.cleaned_data['password']
      user=authenticate(request,email=email,password=password)
      if user is not None:
        login(request,user)
        messages.success(request,"Login succesfully")
        return redirect('home')
      else:
        messages.error(request,'Invalid email or password')
  else:
    form=LoginForm()
  return render(request,'login.html',{'form':form})

def home(request):
    return render(request, 'home.html')