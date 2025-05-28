from flask import Flask, jsonify
import requests

app = Flask(__name__)

from flask import request

@app.route('/baseprice')
def get_base_price():
    symbol = request.args.get('symbol', '').upper()
    if not symbol:
        return jsonify({'error': 'Missing symbol parameter'})

    sheet_url = "https://docs.google.com/spreadsheets/d/16hL7uCokQG5KbEtu-MAZBcUhzO6DASa06sG1_2ROhsI/export?format=csv"
    try:
        response = requests.get(sheet_url)
        lines = response.text.splitlines()

        for row in lines[1:]:  # Skip header
            cells = row.split(',')
            if len(cells) >= 2 and cells[0].strip().upper() == symbol:
                return jsonify({'base_price': float(cells[1])})

        return jsonify({'error': f'Symbol {symbol} not found'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

