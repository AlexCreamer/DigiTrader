from django.apps import AppConfig


class CreditLedgerConfig(AppConfig):
    name = 'Credit_Ledger'

    def ready(self):
        import Credit_Ledger.signals.authentication
