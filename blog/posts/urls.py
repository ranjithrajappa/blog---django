from django.urls import path   #path is a function
from . import views

urlpatterns = [
  
    # path('hello/',views.helloworld,name='helloworld'),
    path('home/',views.home,name="home"),
    path('<int:id>/',views.post,name="post"),
    path('viva/',views.viva,name="viva"),
  
    
]
