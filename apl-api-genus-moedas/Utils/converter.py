import json
from collections import namedtuple


class Converter:

    @staticmethod
    def custom_currency(currency_dict):
        return namedtuple('Currency', currency_dict.keys())(*currency_dict.values())

    @staticmethod
    def custom_currency_decoder(currency_dict):
        return json.loads(currency_dict, object_hook=Converter.custom_currency)

    @staticmethod
    def custom_currency_encoder(currency_object):
        return currency_object.__dict__



