"""ESIwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from Connor import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^topFrame', views.topFrame),
    url(r'^colFrame', views.colFrame),
    url(r'^MenuFrame', views.MenuFrame),
    url(r'^pushRLFrame', views.pushRLFrame),
    url(r'^PageFrame', views.PageFrame),
    url(r'^Page_lwtj', views.Page_lwtj),
    url(r'spiderSen', views.spiderSen),
    url(r'Page_yygx', views.Page_yygx),
    url(r'^Page_lwzl', views.Page_lwzl),
    url(r'^Page_citationFrequency', views.Page_citationFrequency),
    url(r'^Page_JournalImpactFactor', views.Page_JournalImpactFactor),
    url(r'^Page_annualPublications', views.Page_annualPublications),
    url(r'^Page_cooperationTypes', views.Page_cooperationTypes),
    url(r'^Page_lwfb', views.Page_lwfb),
    url(r'^Page_lwhz', views.Page_lwhz),
    url(r'^Page_journalsContribution', views.Page_journalsContribution),
    url(r'^Page_staffsImport', views.Page_staffsImport),
    url(r'^Page_journalsImport', views.Page_journalsImport),



]
