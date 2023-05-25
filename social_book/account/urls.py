from django.urls import path


from . import views

urlpatterns = [
    path("register.html", views.register, name="register"),
    path("register", views.register, name="register"),
    path("login.html", views.login, name="login"),
    path("login", views.login, name="login"),
    path("otp", views.otp, name="otp"),
    path("password", views.password, name="password"),
    path("profile", views.profile, name="profile"),
    path("changepassword", views.changepassword, name="changepassword"),
    path('index.html', views.index, name='index'),
    path('logout', views.logout, name='logout')
]
