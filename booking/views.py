
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

from booking.models import Event, Participant
from booking.forms import  ParticipantSmallForm

import logging
logger = logging.getLogger(__name__)


class ParticipantDetail(DetailView):
    model = Participant
    context_object_name = "participant"


class ParticipantCreate(CreateView):
    form_class = ParticipantSmallForm
    model = Participant

    def get_initial(self):

        event = get_object_or_404(Event, pk = self.kwargs.get('event_id'))    
        return { 'event': event.id,
                 'from_date': event.start_date,
                 'to_date': event.end_date  }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ParticipantCreate, self).form_valid(form)


class ParticipantUpdate(UpdateView):
    form_class = ParticipantSmallForm
    model = Participant


class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('event_list')


class EventList(ListView):
    model = Event


class EventDetail(DetailView):
    model = Event

#    def get_object(self):
#        if self.request.GET.get('date',''):
