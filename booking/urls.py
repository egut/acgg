from django.conf.urls import patterns, url

from booking.views import ParticipantCreate, ParticipantUpdate, ParticipantDelete, ParticipantDetail
from booking.views import EventList, EventDetail

urlpatterns = patterns('booking.views',
	url(r'events/', EventList.as_view(), name = 'event_list'),
	url(r'event/(?P<pk>\d+)/$', EventDetail.as_view(), name = 'event_detail'),

    url(r'add/(?P<event_id>\d+)/$', ParticipantCreate.as_view(), name = 'participant_add'),
    url(r'delete/(?P<pk>\d+)/$', ParticipantDelete.as_view(), name = 'participant_delete'),
    url(r'edit/(?P<pk>\d+)/$', ParticipantUpdate.as_view(), name = 'participant_update'),
	url(r'(?P<pk>\d+)/$', ParticipantDetail.as_view(), name = 'participant_detail')
)

