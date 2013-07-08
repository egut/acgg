from django.db import models
from smart_selects.db_fields import ChainedForeignKey 
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    """ This describ the event in question """

    class Meta:
        db_table = "booking_event"
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


    name = models.CharField(
        max_length = 150, 
        help_text = _("The name of the event"),
        unique = True
        )

    description = models.TextField(
        help_text = _("Describe the event"),
        null = True,
        blank = True
        )

    start_date = models.DateField(
        help_text = _("Start date of the Event")
        )

    end_date = models.DateField(
        help_text = _("End date of the Event")
        )

    def __unicode__(self):
        return "%s"  % (self.name)


class ParticipantLevel(models.Model):
    """ 
    To what level can you perticitate to this event.
    For ACG-G this would normaly be:
       - Visitor : price 20kr
       - No computer : price 80kr
       - With computer: price 100kr

    This is needed as the price will change from year to year. 

    """

    class Meta:
        db_table = "booking_participant_level"
        verbose_name = _("Participant Level")
        verbose_name_plural = _("Participant Levels")

    description = models.CharField( 
        max_length = 50,
        help_text = _("Describe the level of participation, it could be: With Computer, Without computer space")
        )

    price = models.PositiveSmallIntegerField(
        help_text = _("The price for this level")
        )
    
    event = models.ForeignKey('Event', 
        help_text = _("To what event do this affect")
        )

    def __unicode__(self):
        return "%s - %s kr"  % (self.description, self.price)


class Participant(models.Model):
    """
    Who will attend this event.

    """

    class Meta:
        db_table = "booking_participant"
        verbose_name = _("Participant")
        verbose_name_plural = _("Participants")


    user = models.ForeignKey(User, 
        help_text = _("How is attending")
        )

    event = models.ForeignKey('Event', 
        help_text = _("What event to attend")
        )

    date = models.DateField(
        help_text = _("What date to attend")
        )

    level = ChainedForeignKey(ParticipantLevel,
        chained_field = "event",
        chained_model_field = "event", 
        show_all = False, 
        auto_choose = True,
        help_text = _("Particpate level")
        )

    def __unicode__(self):
        return "%s"  % (self.user)