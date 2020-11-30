""" Django."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView, ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail


""" Local."""
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import Profile
from django.conf import settings
from django.template.loader import get_template


class Detail(LoginRequiredMixin, DetailView):
    template_name = "users/detail.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

class Login(auth_views.LoginView):
    """ login view """

    template_name = "users/login.html"
    redirect_authenticated_user = True

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    """ logout view """
     
    template_name = "users/logout.html"


def Signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken == True:
            return render(request, "users/signup.html", {"error": "User already registered"})
        else:
            password = request.POST["password"]
            password_confirmation = request.POST["password_confirmation"]

            if password == password_confirmation:
                form = SignupForm(request.POST)

                if form.is_valid():
                    email = request.POST["email"]
                    context = {"email": email}
                    template = get_template("users/correo.html")
                    content = template.render(context)

                    send_mail("Registro en Proyectoweb", content, settings.EMAIL_HOST_USER , [email])
                    form.save()
                    return redirect('login')
            else:
                return render(request, "users/signup.html", {"error": "Passwords do not match"})
                

    return render(request, 'users/signup.html')


class UpdateProfile(LoginRequiredMixin, UpdateView):

    model = Profile
    fields = ["phone", "biography", "birthdate", "nationality" ,"picture"]
    template_name = "users/update.html"
    context_object_name = "item"
    
    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse("detail",  kwargs={'username': username})


class home(LoginRequiredMixin, ListView):

    template_name = "users/home.html"
    model = Profile
    context_object_name = "profiles"
    queryset = Profile.objects.all()





















# def email(request):
#     if request.method == "POST":
#         titulo = request.POST["titulo"]
#         contenido = request.POST["contenido"]
#         email = request.POST["email"]

#         send_mail(titulo, contenido, settings.EMAIL_HOST_USER , [email])
#         print(titulo, contenido, email)
#         return render(request, "gracias.html")
    
#     return render(request, "email.html")

# class Signup(FormView):
#     """Users sign up view."""

#     template_name = 'users/signup.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         """Save form data."""
#         form.save()
#         return super().form_valid(form)