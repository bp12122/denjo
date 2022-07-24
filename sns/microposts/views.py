from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hope
from .forms import HopeCreateForm, HopeUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class HopeCreateView(LoginRequiredMixin, CreateView):
   template_name = 'microposts/create.html'
   form_class = HopeCreateForm
   success_url = reverse_lazy('microposts:create')
   
   def form_valid(self, form):
       # formに問題なければ、owner id に自分のUser idを割り当てる     
       # request.userが一つのセットでAuthenticationMiddlewareでセットされている。
       form.instance.customer_user_id = self.request.user.id
       messages.success(self.request, '投稿が完了しました')
       return super(HopeCreateView, self).form_valid(form)
"""
   def form_invalid(self, form):
       messages.warning(self.request, '投稿が失敗しました')
       return redirect('microposts:create')
"""

class HopeListView(LoginRequiredMixin, ListView):
    template_name = 'microposts/postlist.html'
    model = Hope
    paginate_by = 10

    def get_queryset(self):
        return Hope.objects.all()

class HopeUpdateView(LoginRequiredMixin, UpdateView): # 追加
   model = Hope
   form_class = HopeUpdateForm
   template_name = 'microposts/update.html'
   
   def form_valid(self, form):
       messages.success(self.request, '更新が完了しました')
       return super(HopeUpdateView, self).form_valid(form)
    
   def get_success_url(self):
       return reverse_lazy('microposts:update', kwargs={'pk': self.object.id})
       
   def form_invalid(self, form):
       messages.warning(self.request, '更新が失敗しました')
       return reverse_lazy('microposts:update', kwargs={'pk': self.object.id})

class HopeDeleteView(LoginRequiredMixin, DeleteView):# 追加
   model = Hope
   template_name = 'microposts/delete.html'
   
   # deleteviewでは、SuccessMessageMixinが使われないので設定する必要あり
   success_url = reverse_lazy('microposts:create')
   success_message = "投稿は削除されました。"
   # 削除された際にメッセージが表示されるようにする。
   def delete(self, request, *args, **kwargs):
       messages.success(self.request, self.success_message)
       return super(HopeDeleteView, self).delete(request, *args, **kwargs)