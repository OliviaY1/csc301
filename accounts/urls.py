from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

urlpatterns = [
    # path('', views.signup_view, name='signup'),
    path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]