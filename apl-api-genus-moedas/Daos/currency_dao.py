from Contexts.mysql_context import MysqlContext
from Models.currency import Currency


class CurrencyDao:

    mysql_context = MysqlContext()

    def save(self, currency):
        try:
            conn = self.mysql_context.mysql_connection()
            cursor = conn.cursor()
            insert = """ INSERT INTO `genus_moedas`.`currency`(`name`,`code`,`value_real`,`value_dollar`,
                        `value_euro`,`timestamp`) VALUES (%s, %s, %s, %s, %s, %s);"""
            params = (
                str(currency.name),
                str(currency.code),
                str(currency.value_real),
                str(currency.value_dollar),
                str(currency.value_euro),
                str(currency.timestamp)
            )
            cursor.execute(insert, params)
            conn.commit()
        except Exception as error:
            raise error
        finally:
            self.mysql_context.mysql_close_connection(cursor, conn)

    def update(self, currency):
        try:
            conn = self.mysql_context.mysql_connection()
            cursor = conn.cursor()
            update = """UPDATE `genus_moedas`.`currency`
                        SET
                        `id_currency` = %s,
                        `name` = %s,
                        `code` = %s,
                        `value_real` = %s,
                        `value_dollar` = %s,
                        `value_euro` = %s,
                        `timestamp` = %s
                        WHERE `code` = %s;"""
            params = (
                str(currency.id_currency),
                str(currency.name),
                str(currency.code),
                str(currency.value_real),
                str(currency.value_dollar),
                str(currency.value_euro),
                str(currency.timestamp),
                str(currency.code)
            )

            cursor.execute(update, params)

            conn.commit()
        except Exception as error:
            raise error
        finally:
            self.mysql_context.mysql_close_connection(cursor, conn)

    def return_by_code(self, code):
        try:
            conn = self.mysql_context.mysql_connection()
            cursor = conn.cursor()
            select = """SELECT `currency`.`id_currency`, `currency`.`name`, `currency`.`code`, `currency`.`value_real`,
                        `currency`.`value_dollar`,`currency`.`value_euro`, `currency`.`timestamp`
                        FROM `genus_moedas`.`currency`
                        WHERE `currency`.`code` = %s"""
            params = (str(code),)
            cursor.execute(select, params)
            registers = cursor.fetchall()
            currency = Currency()
            if registers:
                for register in registers:
                    currency.id_currency = register[0]
                    currency.name = register[1]
                    currency.code = register[2]
                    currency.value_real = register[3]
                    currency.value_dollar = register[4]
                    currency.value_euro = register[5]
                    currency.timestamp = register[6]
                return currency
            else:
                return None
        except Exception as error:
            raise error
        finally:
            self.mysql_context.mysql_close_connection(cursor, conn)

    def return_all(self):
        try:
            conn = self.mysql_context.mysql_connection()
            cursor = conn.cursor()
            select = """SELECT `currency`.`id_currency`, `currency`.`name`, `currency`.`code`, `currency`.`value_real`,
                        `currency`.`value_dollar`,`currency`.`value_euro`, `currency`.`timestamp`
                        FROM `genus_moedas`.`currency`"""
            cursor.execute(select)
            registers = cursor.fetchall()
            currencies = []
            if registers:
                for register in registers:
                    currency = Currency()
                    currency.id_currency = register[0]
                    currency.name = register[1]
                    currency.code = register[2]
                    currency.value_real = register[3]
                    currency.value_dollar = register[4]
                    currency.value_euro = register[5]
                    currency.timestamp = register[6]
                    currencies.append(currency)
                return currencies
            else:
                return None
        except Exception as error:
            raise error
        finally:
            self.mysql_context.mysql_close_connection(cursor, conn)

    def delete_all(self):
        try:
            conn = self.mysql_context.mysql_connection()
            cursor = conn.cursor()
            delete = """ DELETE FROM `genus_moedas`.`currency`; """
            cursor.execute(delete)
            conn.commit()
        except Exception as error:
            raise error
        finally:
            self.mysql_context.mysql_close_connection(cursor, conn)