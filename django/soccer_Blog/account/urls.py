from django.urls import path
from account import views as account_views

urlpatterns = [
    path("login/", account_views.login_view, name="login"), 
    path("logout/", account_views.logout_view, name="logout"), 
    path("register/", account_views.register_view, name="register"), 
]