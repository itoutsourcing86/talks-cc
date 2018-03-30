from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from braces import views
from talks.models import TalkList


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.CreateView):
    form_valid_message = 'You are already registered!'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        TalkList.objects.create(user=self.object, name='To Attend')
        return resp


class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')
    form_valid_message = 'You are already logged in!'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user.is_active and user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(views.LoginRequiredMixin, views.MessageMixin, generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.messages.success = 'You\'ve been logged out. Come back soon!'
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
