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
	url(r'^admin/', admin.site.urls),
	url(r'^$', appone_views.index, name = 'default'),
	url(r'^index$', appone_views.index, name = 'index'),
	url(r'^main$', appone_views.main, name='main'),
	url(r'^add_model/$', appone_views.add_model, name='add_model'),
	url(r'^history$', appone_views.history, name='history'),
	url(r'^lstm$', appone_views.lstm, name='lstm'),
	url(r'^lstm_guard/$', appone_views.lstm_guard, name='lstm_guard'),
    url(r'^main_guard/$', appone_views.main_guard, name='main_guard'),
	url(r'^relation$', appone_views.relation, name='relation'),
	url(r'^galaxy$', appone_views.galaxy, name='galaxy'),

	url(r'^thresold/$', appone_views.thresold, name='thresold'),
	url(r'^prediction$', appone_views.prediction, name='prediction'),
	url(r'^recordnumber$', appone_views.recordnumber, name='recordnumber'),
	url(r'^guard_test$', appone_views.guard_test, name='guard_test'),
    url(r'^guard_kdd$', appone_views.guard_kdd, name='guard_kdd'),
	url(r'^add_LSTM/$', appone_views.add_LSTM, name='add_LSTM'),
	url(r'^add_Ralation/$', appone_views.add_Ralation, name='add_Raletion'),
	url(r'^add_GUARD/$', appone_views.add_GUARD, name='add_GUARD'),
	url(r'^simulate$', appone_views.simulate, name='simulate'),

	url(r'^load_model/$', appone_views.load_model, name = 'load_model'),
	url(r'^load_agent/$', appone_views.load_agent, name = 'load_agent'),
	url(r'^load_guard/$', appone_views.load_guard, name = 'load_guard'),
    url(r'^search/$', appone_views.search, name = 'search'),
	url(r'^analyse_lstm/$', appone_views.analyse_lstm, name = 'analyse_lstm'),
	url(r'^analyse_lstm_g/$', appone_views.analyse_lstm_g, name = 'analyse_lstm_g'),
	url(r'^analyse_lstm_g_all/$', appone_views.analyse_lstm_g_all, name = 'analyse_lstm_g_all'),
	url(r'^feature_extract/$', appone_views.feature_extract, name = 'feature_extract'),
	url(r'^analyse_fp/$', appone_views.analyse_fp, name = 'analyse_fp'),
	url(r'^analyse_OO/$', appone_views.analyse_OO, name = 'analyse_OO'),
	url(r'^analyse_PP/$', appone_views.analyse_PP, name = 'analyse_PP'),
]

