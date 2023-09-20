from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from core.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')), # All urls that begin with dashboard will be handled by dashboard/urls.py
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/', include('userprofile.urls')),
    path('about/', about, name='about'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
