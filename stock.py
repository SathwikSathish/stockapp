from flask import Flask, request, jsonify
import requests

app = Flask("stockdata")

# Stock Data API Endpoint and API Token
STOCK_API_URL = "https://api.stockdata.org/v1/data/quote"
API_TOKEN = "NOFm0ZKYjli9oN9J27St1vNnvj0vhvG2126GXWcr"  # Replace with your actual API token
DEFAULT_SYMBOL = "AAPL"

@app.route('/get-stock', methods=['GET'])
def get_stock():
    """Fetch the most recent stock data for the given symbol."""
    # Get stock symbol from query parameters or use default
    symbol = request.args.get('symbol', DEFAULT_SYMBOL).upper()

    if not symbol:
        return jsonify({"error": "Stock symbol is required!"}), 400

    # Set headers and parameters for the API request
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"symbols": symbol}

    try:
        # Make the API request to fetch stock data
        response = requests.get(STOCK_API_URL, headers=headers, params=params)

        # Handle successful response
        if response.status_code == 200:
            data = response.json()

            # Check if data is available
            if data.get('data'):
                stock_info = data['data'][0]  # Assuming the most recent data is the first one
                return jsonify(stock_info), 200
            else:
                return jsonify({"error": "No data found for the given symbol!"}), 404

        # Handle errors from the API
        else:
            return jsonify({
                "error": "Failed to fetch stock data.",
                "details": response.json()
            }), response.status_code

    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


app.run(debug=True)