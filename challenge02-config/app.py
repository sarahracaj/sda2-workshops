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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=DEBUG_MODE)
