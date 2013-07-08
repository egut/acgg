from django import forms
from booking import models as booking_models

class EventForm(forms.ModelForm):
	"""
	Describe master Event form 
	"""
	class Meta:
		model = booking_models.Event
        fields = ('name','description','start_date','end_date') 



class ParticipantLevelForm(forms.ModelForm):
	"""
	Describe master ParticipantLevel form 
	"""

	class Meta:
		model = booking_models.ParticipantLevel
		fields = ('description','price','event') 


class ParticipantForm(forms.ModelForm):
	"""
	Describe master Participant form 
	"""

	class Meta:
		model = booking_models.Participant
		fields = ('user','event','date','level') 

              