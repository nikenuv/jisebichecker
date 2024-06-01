from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("viewProfile/", views.user_profile, name="profile"),
    path('editProfile/', views.edit_profile, name='editProfile'),
    path('logout/', views.log_out, name='logout'),
]
