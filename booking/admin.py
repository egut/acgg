# -*- coding: utf-8 -*-
from booking import models, forms
from django.contrib import admin


class ParticipantLevelInlineAdmin(admin.TabularInline):
    """ Make the ParticipantLevel a inline admin module to Event """
    model = models.ParticipantLevel


class EventAdmin(admin.ModelAdmin):
    """ Event Admin interface """
    form = forms.EventForm
    inlines = [ParticipantLevelInlineAdmin,]


class ParticipantAdmin(admin.ModelAdmin):
    """ Participant Admin interface """
    form = forms.ParticipantForm

    list_display = ('event', 'user', 'from_date', 'to_date', 'level')
    list_filter = ('event',)
    search_fields = ['event__name', 'user__first_name', 'user__last_name', 'from_date', 'to_date']



admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Participant, ParticipantAdmin)

