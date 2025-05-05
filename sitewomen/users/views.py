from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from users.forms import LoginUserForm


# Create your views here.

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#
#     return render(request, 'users/login.html', context={'form': form})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title': "Авторизация"
    }

    def get_success_url(self):
        return reverse_lazy('add_page')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


