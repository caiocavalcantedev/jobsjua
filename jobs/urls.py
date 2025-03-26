from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('view_vacancies/', views.view_vacancies, name='view_vacancies'),
    path('view_one_vacancie/<int:id>/', views.view_one_vacancie, name='view_one_vacancie'),
]