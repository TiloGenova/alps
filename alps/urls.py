from django.contrib import admin
from django.urls import path
from alps import views

app_name ='alps'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sports/', views.sports, name='sports'),
    path('contatti/', views.contatti, name='contatti'),
    path('luoghi/', views.luoghi, name='places'),
    path('alps/<int:activity_id>', views.details, name='details'),



]