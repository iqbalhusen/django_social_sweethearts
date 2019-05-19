from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('logout/', views.logout_view),
    path('de_auth_callback/', views.de_auth_callback)
]
