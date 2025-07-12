from django.urls import path
from . import views

urlpatterns = [
    # ...existing urls...
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
]