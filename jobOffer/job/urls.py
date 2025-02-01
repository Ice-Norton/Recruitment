from django.urls import path
from .views import login, register, job_offers, my_applications, apply_now

urlpatterns = [
    path("", job_offers, name="job_offers"),
    path("j", login, name="login"),
    path("r", register, name="register"),
    path("u", my_applications, name="my_applications"),
    path("f", apply_now, name="apply_now")

]
