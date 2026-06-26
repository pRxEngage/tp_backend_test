from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tp_backend_test.users"
    verbose_name = _("Users")

    def ready(self):
        """
        Override this method in subclasses to run code when Django starts.
        """
