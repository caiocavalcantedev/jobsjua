from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('auth/', include('secret.urls'), name='auth'),
]
