from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from booking.menu import EventsMenu

class EventApp(CMSApp):
    name = _("Bookings") 
    urls = ["booking.urls"]
    menus = [EventsMenu]

apphook_pool.register(EventApp) 