from django.urls import path
from . import views

urlpatterns = [
    path('register/',  views.register, name='register'),
    path('login/',views.login , name='login'),
    path('logout/', views.logout, name="logout"),
    path('platform/', views.platform, name='platform'),
    path('platform/new_vacancie/',views.new_vacancie, name="new_vacancie"),
    path('platform/secret_one_vacancie/<int:id>/',views.secret_one_vacancie, name='secret_one_vacancie'),
    path('platform/edit_vacancie/<int:id>', views.edit_vacancie, name="edit_vacancie"),
    path('platform/delete_vacancie/<int:id>', views.delete_vacancie, name="delete_vacancie"),

    # URLS REFERENTE A RECUPERAÇÂO DE SENHAS
    path('recovery_password/', views.recovery_password, name="recovery_password"),
]