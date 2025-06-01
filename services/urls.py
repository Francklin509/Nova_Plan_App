from django.urls import path
from .import views
urlpatterns = [
    path('', views.architechture),
    path('conception/', views.conception),
    path('devis/', views.devis),
    path('inspection/', views.inspection),
    path('modern/', views.modern),
    path('restauration/', views.restauration)
]