from django.urls import path
from .views import LogoutView, app_admin, new_statement, register, LoginView, statements, home_page

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register", register, name="register"),
    path("statements", statements, name="statements"),
    path("new", new_statement, name="new_statement"),
    path("app_admin", app_admin, name="app_admin"),
    path("", home_page, name="home_page"),
]
