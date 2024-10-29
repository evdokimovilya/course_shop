from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("home/", views.profile, name="home"),
    path("change_password/", views.change_password, name="change_password"),
    path("courses/", views.courses, name="courses"),
    path('courses/<int:course_id>/', views.course_learn, name='course_learn'),
]