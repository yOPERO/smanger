from django.conf.urls import patterns, url
from mysm.views import ScreenList, ScreenDetail, ScreenDelete, ScreenCreate, ScreenUpdate
from mysm.views import LinkCreate, LinkDetail, LinkList, LinkDelete, LinkUpdate
from mysm.views import ScreenLinkList, ScreenLinkCreate, ScreenLinkDetail, ScreenLinkDelete, ScreenLinkUpdate, ScreenLinkCreateScreen, NewLink
from mysm.views import getObject
from django.conf.urls import include, url

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('',
	#Screen Views
	url(r'^admin/', include(admin.site.urls)),

	url(r'^screens/$', ScreenList.as_view(), name='screen_list'),
	url(r'^screen/create/$', ScreenCreate.as_view(), name='screen_create'),
	url(r'^screen/(?P<pk>[-\w]+)/detail/$', ScreenDetail.as_view(), name='screen_detail'),
	url(r'^screen/(?P<pk>[0-9]+)/delete/$', ScreenDelete.as_view(), name='screen_delete'),
	url(r'^screen/(?P<pk>[0-9]+)/update/$', ScreenUpdate.as_view(), name='screen_update'),
	#Link Views
	url(r'^links/$', LinkList.as_view(), name='link_list'),
	url(r'^link/create/$', LinkCreate.as_view(), name='link_create'),
	url(r'^link/(?P<pk>[-\w]+)/detail/$', LinkDetail.as_view(), name='link_detail'),
	url(r'^link/(?P<pk>[0-9]+)/delete/$', LinkDelete.as_view(), name='link_delete'),
	url(r'^link/(?P<pk>[0-9]+)/update/$', LinkUpdate.as_view(), name='link_update'),
	#ScreenLink Views
	url(r'^sl/$', ScreenLinkList.as_view(), name='sl_list'),
	url(r'^sl/create/$', ScreenLinkCreate.as_view(), name='sl_create'),
	url(r'^sl/(?P<pk>[-\w]+)/detail/$', ScreenLinkDetail.as_view(), name='sl_detail'),
	url(r'^sl/(?P<pk>[0-9]+)/delete/$', ScreenLinkDelete.as_view(), name='sl_delete'),
	url(r'^sl/(?P<pk>[0-9]+)/update/$', ScreenLinkUpdate.as_view(), name='sl_update'),

	url(r'^sl/create/(?P<pk>[-\w]+)/$', ScreenLinkCreateScreen.as_view(), name='sl_create_with_screen'),
	url(r'^sl/create1/$', NewLink.as_view(), name='newlink'),
	url(r'^sl/json/(?P<id>[0-9]+)/$', getObject, name='json'),




	)
# Change admin site title
admin.site.site_header = _("Ebury's _Digital Signage_")
admin.site.site_title = _("My Site Admin")
admin.site.site_url = _("/admin/mysm/screenlink/")
