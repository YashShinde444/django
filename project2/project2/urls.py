    
from django.conf.urls import url
from django.contrib import admin
from crudapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^load_form/', views.load_form),
    url(r'^add', views.add),
    url(r'^create/', views.create),
    url(r'^show', views.show),
]
