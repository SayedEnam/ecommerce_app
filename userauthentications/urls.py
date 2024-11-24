from django.urls import path
from userauthentications import views

app_name = "userauthentications"

urlpatterns = [
    path("sign-up/", views.register_view, name="sign-up"),
    path("sign-in/", views.login_view, name="sign-in")
]