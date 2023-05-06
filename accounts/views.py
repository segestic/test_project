from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .decorators import unauthenticated_user
from .persist import commit_repo
@unauthenticated_user
def register(request):
    return render(request, '../templates/accounts/register.html')

# @unauthenticated_user
class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/accounts/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        commit_repo('database update')
        return redirect('/')

# @unauthenticated_user

from django.http import HttpResponseRedirect
from django.urls import reverse

@unauthenticated_user
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard-index'))
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
