from django.apps import AppConfig


class CreditLedgerConfig(AppConfig):
    name = 'credits_platform'

    def ready(self):
        import credits_platform.signals.custom_auth
