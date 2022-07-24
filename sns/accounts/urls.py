from django.urls import path
from .views import (
   RegistUserView,HomeView, 
   UserLoginView, UserLogoutView, #追加
   ProfileEditView,UserListView, # 追加
)
app_name = 'accounts'
urlpatterns = [
   path('home/', HomeView.as_view(), name='home'),
   path('regist/', RegistUserView.as_view(), name='regist'),
   path('login/', UserLoginView.as_view(), name='login'), #追加
   path('logout/', UserLogoutView.as_view(), name='logout'),  #追加 
   path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'), # 追加
   path('userlist/', UserListView.as_view(), name='userlist'), # 追加
]
