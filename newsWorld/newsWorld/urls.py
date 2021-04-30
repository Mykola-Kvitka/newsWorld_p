from django.contrib import admin
from django.urls import path
from firstapp import views
from django.urls import re_path
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('news/<int:id>/', views.getCertainNews),
    path('topics/<int:id>/', views.getCertainTopic),
    path('accounts/', include('django.contrib.auth.urls')),  
    path("register/", views.register_request, name='registr')

]
