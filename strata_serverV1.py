from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/baseprice')
def get_base_price():
    sheet_url = 'https://docs.google.com/spreadsheets/d/e/your-sheet-id/pub?output=csv'
    try:
        response = requests.get(sheet_url)
        lines = response.text.splitlines()
        value = lines[1].split(',')[0]
        return jsonify({'base_price': float(value)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
