from flask import abort
from Services.currency_service import CurrencyService


class CurrencyController:

    currency_service = CurrencyService()

    def search_all_currencies(self):
        try:
            return self.currency_service.return_currencies_list()
        except Exception as error:
            raise error

    def update_currencies_values(self):
        try:
            self.currency_service.return_live('USD')
            self.currency_service.fill_euro_value()
            self.currency_service.fill_real_value()
            currencies = self.currency_service.return_all_currencies_live()
            return currencies
        except Exception as error:
            raise error

    def convert(self, source, target, value):
        try:
            if not source:
                abort(500)
            if not target:
                abort(500)
            if not value:
                abort(500)
            value_target = {
                'value_target': self.currency_service.convert_currencies(source, target, float(value))
            }
            return value_target
        except Exception as error:
            raise error

