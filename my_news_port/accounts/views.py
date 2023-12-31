from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import CunstomSignupForm


class SignUp(CreateView):
    model = User
    form_class = CunstomSignupForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

