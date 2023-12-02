# yourapp/urls.py
from django.urls import path
#from .views import login_view
from .views import signup,login

urlpatterns = [
    #path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]