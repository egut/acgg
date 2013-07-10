
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.forms.models import modelformset_factory

from booking.models import Event, ParticipantLevel, Participant
from booking.forms import ParticipantForm

import logging
logger = logging.getLogger(__name__)

def list_events(request):
	"""
	List all known events.
	"""
	pass

def event(request, event_id):
	"""
	List one event and all participants
	"""
	pass

@login_required
def manage_booking(request, event_id):
	"""
	Book you self into one event
	"""

	event = get_object_or_404(Event,pk = event_id)

	ParticipantFormSet = modelformset_factory(Participant,form = ParticipantForm, can_delete = True)
	if request.method == "POST":
		formset = ParticipantFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
		else:
			logger.error("Formset isn't valid")
	else:
		formset = ParticipantFormSet(queryset = Participant.objects.filter(user = request.user, event = event),
		 	initial=[{'user':request.user, 'event':event.id},{'user':request.user, 'event':event.id}])

	return render(request, 
		"booking/manage_booking.html", 
		{"formset": formset,
		})



@login_required
def manage_booking_old(request, event_id):
	"""
	Book you self into one event
	"""

	event = get_object_or_404(Event,pk = event_id)

	ParticipantInlineFormSet = inlineformset_factory(Event, 
		Participant,
		form = ParticipantForm)

	user = request.user
	for form in ParticipantInlineFormSet.forms:
	    if 'user' not in form.initial:
	        form.initial['user'] = user.pk

	if request.method == "POST":
		formset = ParticipantInlineFormSet(request.POST, request.FILES, instance = event)
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(event.get_absolute_url())
	else:
		formset = ParticipantInlineFormSet(instance = event)

	return render(request, 
		"booking/manage_booking.html", 
		{"formset": formset,
		})

