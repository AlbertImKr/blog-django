from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("signin")
    success_message = "가입이 완료되었습니다. 축하합니다!"


class SignInView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signin.html"
    success_url = reverse_lazy("home")
    success_message = "로그인 되었습니다. 환영합니다!"
