from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts_home'),  # Example route
]