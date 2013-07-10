from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from booking.models import EventPlugin as EventPluginModel
from django.utils.translation import ugettext as _

class EventPlugin(CMSPluginBase):
    model = EventPluginModel
    name = _("Event Booking Plugin")
    render_template = "booking/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(EventPlugin)