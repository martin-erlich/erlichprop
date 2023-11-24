from helper.pdf import *
from helper.scraper import *
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)


@app.route('/zona_prop', methods=['GET'])
def get_zona_prop():
    body = request.get_json()
    url = body['url']
    return jsonify(get_zona_prop_info(url))
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # app.run(host='0.0.0.0',debug=True,port=3000)

    # https://erlich-prop-scrapper-9e17f7c92865.herokuapp.com