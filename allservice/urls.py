from django.urls import path

from . import views

urlpatterns = [
    path("", views.All_Service.as_view(), name="home-page"),
    path("register", views.RegisterPage.as_view(), name="register-page"),
    path("confirm_email/", views.ConfirmEmailAuthentication, name="confirm-email"),
    path("login", views.Login.as_view(), name="login-page"),
    path("logout", views.Logout.as_view(), name="logout-page"),
    path("account",  views.AccountInfo.as_view(), name="account-page"),
    path("forgot_password", views.ForgotPassword.as_view(), name="forgot-password"),
    path("password_reset" , views.PasswordReset.as_view(), name="password-reset"),
    path("transaction_start", views.TransactionStart.as_view(), name="transaction-start-page")
]

