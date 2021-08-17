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
#app_name = 'measurement_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('office/', views.all_office, name='office'),
    path('last/', views.last_entry_view, name='last_entry'),
]