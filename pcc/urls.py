"""pcc URL Configuration

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
from appone import views as appone_views

urlpatterns = [
	url(r'^$', appone_views.index, name='first'),
	url(r'^main$', appone_views.main,name='main'),
	url(r'^single$', appone_views.single, name='single'),
	url(r'^relation$', appone_views.relation,name='relation'),
	url(r'^index$', appone_views.index),
    url(r'^admin/', admin.site.urls),
	url(r'^prediction/$', appone_views.prediction, name='prediction'),
	url(r'^recordnumber/$', appone_views.recordnumber, name='recordnumber'),
	url(r'^addconfiguretodatabase/', appone_views.addconfiguretodatabase),
	url(r'^addok/', appone_views.addok),
	url(r'^addconfigure/', appone_views.addconfigure),
	url(r'^simulate/', appone_views.simulate, name='simulate'),

	url(r'^history', appone_views.history),
	url(r'^load_model/', appone_views.load_model),
    url(r'^search/', appone_views.search),
	url(r'^addconfiguretodatabaseRelation/', appone_views.addconfiguretodatabaseRelation),
	url(r'^addok2/', appone_views.addok2),
	url(r'taiyangxi_small$', appone_views.taiyangxi, name='taiyangxi_small'),
	url(r'^analyse_lstm/', appone_views.analyse_lstm),
	url(r'^analyse_fp/', appone_views.analyse_fp),
]

