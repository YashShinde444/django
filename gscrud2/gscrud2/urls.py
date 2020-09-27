"""gscrud2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from enroll import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^add/', views.add_show,name="addandshow"),
    url(r'^add/', views.UserAddShowView.as_view(),name="addandshow"),
    #url(r'^delete/(?P<id>\d+)/$', views.delete_data,name="deletedata"),
    url(r'^delete/(?P<id>\d+)/$', views.UserDeleteView.as_view(),name="deletedata"),
    url(r'^update/(?P<id>\d+)/$', views.UserUpdateView.as_view(),name="updatedata"),
]
