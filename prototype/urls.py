'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('new_app.urls')),
]
'''
from django.urls import path
from . import views
#app_name = t_app
urlpatterns = [
    path('', views.index, name='index'),
]