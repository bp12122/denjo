from django.db import models
from django.contrib.auth.models import (
   BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy

# Create your models here.
class UserManager(BaseUserManager):
   def create_user(self, username, email, password=None):
       if not email:
           raise ValueError('Enter Email') # エラーメッセージ
       user = self.model(
           username=username,
           email=email
       )
       user.set_password(password) # passwordを引数にとってパスワード設定
       user.save(using=self._db) # データベースへユーザーを保存
       return user
   def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
           username,
           email,
           password=password,
        )
        user.staff = True
        user.admin = True
        user.super = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
   username = models.CharField(max_length=50, unique=True)
   email = models.EmailField(max_length=50, unique=True)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   shop_flag = models.BooleanField(default=0)
   shop_url = models.URLField(max_length=200, null=True, blank=True)
   customer_age = models.IntegerField(default=0, null=True, blank=True)
   tel = models.CharField(max_length=11)
   # プロフィール画像をavatarとして設定
   avatar = models.ImageField(blank=True, null=True)  
   EMAIL_FIELD = 'email'
   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email'] 
   
   objects = UserManager()
   
   def get_absolute_url(self):
       return reverse_lazy('accounts:home')