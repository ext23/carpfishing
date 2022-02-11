from django.apps import AppConfig


class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persons'


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'


class JudgesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'judges'
