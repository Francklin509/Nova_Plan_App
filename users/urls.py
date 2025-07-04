from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.user_login),
    path('registration/', views.registration),
    path('dashboard/', views.dashboard),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_management),
    path('payment/', views.payment)
]