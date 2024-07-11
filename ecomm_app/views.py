from django.shortcuts import render
from .forms import RegisterForm
from django.views import View
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


class RegistrationView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'customer_registration.html',locals())
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
        else:
            messages.warning(request, 'Something went wrong')
            return render(request,'customer_registration.html',locals())