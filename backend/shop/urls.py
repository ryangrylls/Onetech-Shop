from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('cart/', CartView.as_view(), name='cart'),
]