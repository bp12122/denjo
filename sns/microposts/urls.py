from django.urls import path
from .views import (
   HopeCreateView, HopeListView,
   HopeUpdateView, HopeDeleteView
)
app_name = 'microposts'
urlpatterns = [
   path('create/', HopeCreateView.as_view(), name='create'),
   path('postlist/', HopeListView.as_view(), name='postlist'),
   path('update/<int:pk>', HopeUpdateView.as_view(), name='update'),
   path('delete/<int:pk>', HopeDeleteView.as_view(), name='delete'),
]