# urls.py
from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload, name="upload"),
    path("report/<str:url>", views.report, name="report"),
    path("report/<str:url>/full", views.full_report, name="full-report"),
    path("report/<str:url>/download", views.download, name="download"),
    path("history", views.history, name="history"),
    path("history/search", views.search_history, name="search")
]
