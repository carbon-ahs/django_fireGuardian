from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/', include('measurement_app.urls')),
    path('', include('prototype.urls')),
]