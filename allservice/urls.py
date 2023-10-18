from django.urls import path

from . import views

urlpatterns = [
    path("", views.All_Service.as_view(), name="home-page"),
    path("register", views.RegisterPage.as_view(), name="register-page"),
    path("confirm_email/", views.ConfirmEmailAuthentication, name="confirm-email"),
    path("login", views.Login.as_view(), name="login-page")
]