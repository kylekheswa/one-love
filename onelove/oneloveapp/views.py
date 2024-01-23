from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views import View
from .models import BlogPost


def home(request):
    return render(request, 'oneloveapp/home.html')

def about(request):
    return render(request, 'oneloveapp/about.html')

def support(request):
    return render(request, 'oneloveapp/support.html')

@login_required(login_url='/registration/login.html/')  
def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'oneloveapp/blog.html', {'posts': posts})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

custom_login = CustomLoginView.as_view()

class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
