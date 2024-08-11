"""Base config for base module."""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    Sets `default_auto_field` to `django.db.models.BigAutoField`
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "wcms.base"
