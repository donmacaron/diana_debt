from django.urls import path, include
import django.contrib.auth.urls
from . import views


urlpatterns = [
    path('', views.show, name = 'home'),
    path('accounts/', include('django.contrib.auth.urls'), name = 'accounts')
]
