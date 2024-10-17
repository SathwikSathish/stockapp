from flask import Flask, request, jsonify, render_template
import requests

app = Flask("stockdata")

STOCK_API_URL = "https://api.stockdata.org/v1/data/quote"
API_TOKEN = "NOFm0ZKYjli9oN9J27St1vNnvj0vhvG2126GXWcr"
DEFAULT_SYMBOL = "AAPL"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-stock', methods=['GET'])
def get_stock():
    symbol = request.args.get('symbol', DEFAULT_SYMBOL).upper()

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"symbols": symbol}

    try:
        response = requests.get(STOCK_API_URL, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('data'):
                stock_info = data['data'][0]
                return jsonify(stock_info), 200
            else:
                return jsonify({"error": "No data found for the given symbol!"}), 404
        else:
            return jsonify({
                "error": "Failed to fetch stock data.",
                "details": response.json()
            }), response.status_code
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

app.run(debug=True)
