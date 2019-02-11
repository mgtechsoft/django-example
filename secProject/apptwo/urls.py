from django.conf.urls import url
from apptwo import views

urlpatterns = [
    url('',views.index,name='index'),
  
]