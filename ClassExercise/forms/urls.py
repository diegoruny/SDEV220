from django.urls import path, include
from . import views

app_name = 'forms'
urlpatterns = [
    path("register/", views.register, name="register"),
    path("", include('django.contrib.auth.urls'))
]
