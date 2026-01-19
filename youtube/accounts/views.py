from django.shortcuts import redirected
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirected('/')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return redirected("/")