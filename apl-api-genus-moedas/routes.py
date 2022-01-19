from flask import Flask
from flask import jsonify
from flask import request
from Controllers.currency_controller import CurrencyController
from Utils.error import Error

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route("/search-all-currencies", methods=['GET'])
def search_all_currencies():
    currency_controller = CurrencyController()
    return jsonify(currency_controller.search_all_currencies())


@app.route("/update-currencies-values", methods=['GET'])
def update_currencies_values():
    currency_controller = CurrencyController()
    return jsonify(currency_controller.update_currencies_values())


@app.route("/convert", methods=['GET'])
def convert():
    currency_controller = CurrencyController()
    source = request.args.get('source')
    target = request.args.get('target')
    value = request.args.get('value')
    return jsonify(currency_controller.convert(source, target, value))


@app.errorhandler(404)
def error_404(error):
    error_util = Error()
    error = error_util.raise_error(404, 'Not found')
    return jsonify(error)


@app.errorhandler(401)
def error_401(error):
    error_util = Error()
    error = error_util.raise_error(401, 'Unauthorized')
    return jsonify(error)


@app.errorhandler(500)
def error_500(error):
    error_util = Error()
    error = error_util.raise_error(500, 'Internal Server Error')
    return jsonify(error)

