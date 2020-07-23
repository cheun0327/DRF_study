from django.urls import path
from rooms import views as room_views

# this app_name must match with config > urls namespace
app_name = "core"

urlpatterns = [
    path("", room_views.home, name="home"),
]

