from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class CoreConfig(AppConfig):
    name = 'core'

class AppAdminConfig(AdminConfig):
    default_site = 'core.admin.AppAdmin'
