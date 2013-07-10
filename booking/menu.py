from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from booking.models import Event

class EventsMenu(CMSAttachMenu):
    name = _("Event Menu")

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for event in Event.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument.
            node = NavigationNode(
                event.name,
                reverse('event_detail', args=(event.pk,)),
                event.pk
            )
            nodes.append(node)
        return nodes
menu_pool.register_menu(EventsMenu) # register the menu.