from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:plant_id>/", views.show_plant, name="show_plant"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register_user/", views.register_user, name="register_user"),
]