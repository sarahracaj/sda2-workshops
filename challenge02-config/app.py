"""
SDA2 Challenge 2: Configuration Management
Demonstrates externalized configuration using environment variables
"""

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read configuration from environment variables
API_KEY = os.getenv('API_KEY', 'default-key')
DEBUG_MODE = os.getenv('DEBUG', 'false').lower() == 'true'

# Optional: Add more config variables
SERVICE_NAME = os.getenv('SERVICE_NAME', 'SDA2 Challenge 2')
MAX_REQUESTS = int(os.getenv('MAX_REQUESTS', '100'))

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": SERVICE_NAME,
        "status": "running",
        "endpoints": ["/config", "/protected"]
    })

@app.route('/config', methods=['GET'])
def get_config():
    """
    Show current configuration (without revealing secrets)
    """
    return jsonify({
        "api_key_set": bool(API_KEY != 'default-key'),
        "debug_mode": DEBUG_MODE,
        "service_name": SERVICE_NAME,
        "max_requests": MAX_REQUESTS
    })

@app.route('/protected', methods=['GET'])
def protected_endpoint():
    """
    Example of API key authentication
    Usage: curl -H "X-API-Key: your-key" https://YOUR-URL/protected
    """
    provided_key = request.headers.get('X-API-Key')
    
    if not provided_key:
        return jsonify({"error": "Missing API key"}), 401
    
    if provided_key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 403
    
    return jsonify({
        "message": "Access granted",
        "secret_data": "This is protected information"
    })

# TODO: Add /weather endpoint that uses WEATHER_API_KEY
# Your code goes below this line

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Simulated weather endpoint that requires WEATHER_API_KEY.
    Returns an error if the key is missing.
    """
    weather_api_key = os.getenv('WEATHER_API_KEY')

    if not weather_api_key:
        return jsonify({"error": "Missing WEATHER_API_KEY environment variable"}), 500

    # Optionally: read a 'city' query param, default to 'Bern'
    city = request.args.get('city', 'Bern')

    # Simulate a weather response (instead of calling a real API)
    fake_weather_data = {
        "city": city,
        "temperature": "15°C",
        "condition": "Cloudy",
        "source": "Simulated Data"
    }

    return jsonify(fake_weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=DEBUG_MODE)
