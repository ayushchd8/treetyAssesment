from django.urls import path
from . import views

app_name = 'companies'
urlpatterns = [
    path('', views.abc, name='abc'),
    path('home/', views.home, name='home'),
    path('companies/', views.companies, name='companies'),
    path('addcompany/', views.addcompany, name='addcompany'),
    path('savecompany/', views.savecompany, name='savecompany'),
]
