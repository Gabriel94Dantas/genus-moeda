from Constants.constants import Contants
from Models.currency import Currency
from Daos.currency_dao import CurrencyDao
from datetime import datetime, timezone
import requests


class CurrencyService:

    constant = Contants()
    currency_dao = CurrencyDao()

    def return_currencies_list(self):
        try:
            url = self.constant.API_CURRENCY_URL + self.constant.LIST_ENDPOINT
            params = {'access_key': self.constant.TOKEN}
            response = requests.get(url, params=params)
            currencies = self.convert_into_currencies_list(response.json()['currencies'])
            self.delete_all()
            for currency in currencies:
                self.save_currency(currency)
            return self.convert_currencies_into_dict_list(currencies)
        except requests.RequestException as error:
            raise error

    def return_live(self, source):
        try:
            url = self.constant.API_CURRENCY_URL + self.constant.LIVE_ENDPOINT
            params = {
                'access_key': self.constant.TOKEN,
                'source': source,
                'format': 1
            }
            response = requests.get(url, params=params)
            quotes = response.json()['quotes']
            currencies = self.convert_into_currencies_list_quotes(quotes, source)
            for currency in currencies:
                self.update_currency(currency)
            return self.convert_currencies_into_dict_list(currencies)
        except requests.RequestException as error:
            raise error

    def save_currency(self, currency):
        try:
            now = datetime.now(timezone.utc)
            currency.timestamp = now
            self.currency_dao.save(currency)
        except Exception as error:
            raise error

    def update_currency(self, currency):
        try:
            now = datetime.now(timezone.utc)
            currency.timestamp = now
            self.currency_dao.update(currency)
        except Exception as error:
            raise error

    def delete_all(self):
        try:
            self.currency_dao.delete_all()
        except Exception as error:
            raise error

    def return_currency_by_code(self, code):
        try:
            currency = self.currency_dao.return_by_code(code)
            return currency
        except Exception as error:
            raise error

    def convert_into_currencies_list_quotes(self, currencies_json, source):
        currencies = []
        if source == 'USD':
            for key in currencies_json:
                if key != source + source:
                    db_key = str(key).replace(source, "")
                    currency = self.return_currency_by_code(db_key)
                    currency.value_dollar = 1/currencies_json[key]
                else:
                    currency = self.return_currency_by_code(source)
                    currency.value_dollar = 1.0
                currencies.append(currency)

        return currencies

    def return_all_currencies(self):
        try:
            return self.currency_dao.return_all()
        except Exception as error:
            raise error

    def return_all_currencies_live(self):
        try:
            currencies = self.return_all_currencies()
            return self.convert_currencies_into_dict_list(currencies)
        except Exception as error:
            raise error

    def fill_euro_value(self):
        try:
            currencies = self.return_all_currencies()
            euro_currency = self.return_currency_by_code('EUR')
            for currency in currencies:
                currency.value_euro = currency.value_dollar/euro_currency.value_dollar
                self.update_currency(currency)
        except Exception as error:
            raise error

    def fill_real_value(self):
        try:
            currencies = self.return_all_currencies()
            real_currency = self.return_currency_by_code('BRL')
            for currency in currencies:
                currency.value_real = currency.value_dollar/real_currency.value_dollar
                self.update_currency(currency)
        except Exception as error:
            raise error

    def convert_currencies(self, source, target, value):
        try:
            currency_source = self.return_currency_by_code(source)
            currency_target = self.return_currency_by_code(target)
            if target == 'USD':
                value_target = float(currency_source.value_dollar) * value
                return value_target
            if target == 'EUR':
                value_target = float(currency_source.value_euro) * value
                return value_target
            if target == 'BRL':
                value_target = float(currency_source.value_real) * value
                return value_target

            value_target = (float(currency_source.value_dollar) / float(currency_target.value_dollar)) * value
            return value_target

        except Exception as error:
            raise error

    @staticmethod
    def convert_currencies_into_dict_list(currencies):
        currencies_json = []
        for currency in currencies:
            currencies_json.append(currency.__dict__)
        return currencies_json

    @staticmethod
    def convert_into_currencies_list(currencies_json):
        currencies = []
        for key in currencies_json:
            currency = Currency()
            currency.code = key
            currency.name = currencies_json[key]
            currencies.append(currency)
        return currencies
