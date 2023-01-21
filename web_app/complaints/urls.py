from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('resolve_issue', views.resolve_issue, name='resolve_issue'),
    path('kpis', views.kpis, name='kpis'),
    path('get_cities', views.get_cities, name='get_cities'),
    path('get_districts', views.get_districts, name='get_districts'),
    
]
