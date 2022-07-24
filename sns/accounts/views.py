from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView 
from django.views.generic.base import TemplateView
from .forms import RegistForm, LoginForm, ProfileForm 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import User # 追加
class HomeView(TemplateView):
   template_name = 'accounts/home.html'
class RegistUserView(CreateView):
   template_name = 'accounts/regist.html'
   form_class = RegistForm
class UserLoginView(LoginView):  
   template_name = 'accounts/login.html'
   authentication_form = LoginForm
class UserLogoutView(LogoutView): 
   pass
class ProfileEditView(LoginRequiredMixin, UpdateView): 
   template_name = 'accounts/edit_profile.html'
   model = User
   form_class = ProfileForm
   success_url = '/accounts/edit_profile/'
   def get_object(self):
       return self.request.user

class UserListView(LoginRequiredMixin, ListView): # 追加
   template_name = 'accounts/userlist.html'
   model = User
   def get_queryset(self):
       print(User.objects.all())  # 追加
       return User.objects.all()