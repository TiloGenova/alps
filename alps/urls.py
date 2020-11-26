from django.contrib import admin
from django.urls import path
from alps import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sports/', views.sports, name='sports'),
    path('detail/', views.detail, name='detail'),



]