from django.urls import path
from .import views
urlpatterns = [
    path('', views.registration),
    path('login/', views.login),
    path('profile/', views.profile_management),
    path('payment/', views.payment)
]