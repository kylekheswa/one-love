from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views import View
from .models import BlogPost

def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, 'oneloveapp/home.html')

def about(request):
    """
    View function for the about page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered about page.
    """
    return render(request, 'oneloveapp/about.html')

def support(request):
    """
    View function for the support page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered support page.
    """
    return render(request, 'oneloveapp/support.html')

@login_required(login_url='/registration/login.html/')  
def blog(request):
    """
    View function for the blog page. Requires login.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered blog page with a list of blog posts.
    """
    posts = BlogPost.objects.all()
    return render(request, 'oneloveapp/blog.html', {'posts': posts})

class CustomLoginView(LoginView):
    """
    Custom login view class inheriting from Django's LoginView.

    Attributes:
        template_name (str): The template to render for the login page.
    """
    template_name = 'registration/login.html'

custom_login = CustomLoginView.as_view()

class RegisterView(View):
    """
    View class for user registration.

    Attributes:
        template_name (str): The template to render for the registration page.
    """
    template_name = 'registration/register.html'

    def get(self, request):
        """
        Handles GET requests for the registration page.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Rendered registration page with an empty registration form.
        """
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handles POST requests for user registration.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Redirects to home page upon successful registration,
                          or re-renders the registration page with form errors.
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
