from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('unlogged/', views.index, name="unloggedHomepage"),
    path('logged/', views.indexLogged, name="loggedHomepage"),
    path('manuscripts/', include('apps.manuscripts.urls')),
    path('accounts/', include('apps.accounts.urls')),

]
