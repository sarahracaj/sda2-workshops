"""
SDA2 Challenge 4: Service B - Data Enricher
Receives data and adds enrichment metadata
"""

import logging
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def log_event(event_type, **kwargs):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_type,
        "service": "service-b",
        **kwargs
    }
    logger.info(json.dumps(log_entry))

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Service B - Data Enricher",
        "status": "running",
        "endpoints": ["/enrich"]
    })

@app.route('/enrich', methods=['POST'])
def enrich():
    """
    Enrich incoming data with metadata
    """
    log_event("enrich_request_received")
    
    try:
        data = request.get_json()
        
        if not data:
            log_event("enrich_error", error="No data provided")
            return jsonify({"error": "No data provided"}), 400
        
        # Add enrichment metadata
        data['enriched_at'] = datetime.utcnow().isoformat() + "Z"
        data['enriched'] = True
        
        # Optional: Add more enrichment logic here
        # e.g., data validation, transformation, external API calls
        
        log_event("enrich_success", enriched_fields=list(data.keys()))
        
        return jsonify(data), 200
        
    except Exception as e:
        log_event("enrich_error", error=str(e), error_type=type(e).__name__)
        return jsonify({"error": str(e)}), 500

# TODO: Add authentication
# - Check for API key in headers
# - Return 401 if missing
# - Return 403 if invalid
# Your code goes below this line


if __name__ == '__main__':
    log_event("service_started", port=8080)
    app.run(host='0.0.0.0', port=8080, debug=False)
