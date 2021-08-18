from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('measurement_app.urls')),
    path('t/', include('prototype.urls')),
]