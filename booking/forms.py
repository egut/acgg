from django import forms
from django.utils.translation import ugettext as _
from django.core import exceptions
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


    def clean(self):
        my_date = self.cleaned_data.get('date')
        my_event = self.cleaned_data.get('event')
        between = booking_models.Event.objects.filter(pk = my_event.id).filter(start_date__lte = my_date, end_date__gte = my_date)

        if len(between) == 0:
            
            try: 
                event = booking_models.Event.objects.get(pk = my_event.id)
                msg = _(u"%s: Is invalid need to be between %s and %s" % (my_date, event.start_date, event.end_date))
            except exceptions.ObjectDoesNotExist:
                msg = -(u"%s: Is not a valid date" % (my_date))

            self._errors["date"] = self.error_class([msg])
            del self.cleaned_data['date']
            #raise forms.ValidationError(_("Invalid date given for this event"))

        cleaned_data = super(ParticipantForm, self).clean()
        return cleaned_data