from django.urls import path
from . import views

app_name = "characters"

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/like/', views.like, name="like"),
]