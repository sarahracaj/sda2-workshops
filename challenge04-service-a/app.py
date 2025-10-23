"""
SDA2 Challenge 4: Service A - Data Processor
Demonstrates inter-service communication in a microservices architecture
"""

import os
import logging
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def log_event(event_type, **kwargs):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_type,
        "service": "service-a",
        **kwargs
    }
    logger.info(json.dumps(log_entry))

# Configuration
ENRICHER_SERVICE_URL = os.getenv('ENRICHER_SERVICE_URL', 'http://localhost:8081')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Service A - Data Processor",
        "status": "running",
        "endpoints": ["/aggregate"],
        "enricher_url": ENRICHER_SERVICE_URL
    })

@app.route('/aggregate', methods=['POST'])
def aggregate():
    """
    Receive data, send to Service B for enrichment, return result
    """
    log_event("aggregate_request_received")
    
    try:
        data = request.get_json()
        
        if not data:
            log_event("aggregate_error", error="No data provided")
            return jsonify({"error": "No data provided"}), 400
        
        log_event("calling_enricher_service", url=ENRICHER_SERVICE_URL)
        
        # Call Service B
        response = requests.post(
            f"{ENRICHER_SERVICE_URL}/enrich",
            json=data,
            timeout=5  # 5 second timeout
        )
        
        if response.status_code != 200:
            log_event("enricher_service_error", 
                     status_code=response.status_code,
                     response=response.text)
            return jsonify({"error": "Enricher service failed"}), 502
        
        enriched_data = response.json()
        
        # Add our own metadata
        enriched_data['processed_by'] = 'service-a'
        
        log_event("aggregate_success", 
                 enriched_fields=list(enriched_data.keys()))
        
        return jsonify(enriched_data), 200
        
    except requests.exceptions.Timeout:
        log_event("enricher_service_timeout")
        return jsonify({"error": "Enricher service timeout"}), 504
    
    except requests.exceptions.ConnectionError:
        log_event("enricher_service_unreachable")
        return jsonify({"error": "Enricher service unreachable"}), 503
    
    except Exception as e:
        log_event("aggregate_error", error=str(e), error_type=type(e).__name__)
        return jsonify({"error": str(e)}), 500

# TODO: Add error handling improvements
# - Retry logic with exponential backoff
# - Circuit breaker pattern
# - Fallback response when Service B is down
# Your code goes below this line


if __name__ == '__main__':
    log_event("service_started", port=8080, enricher_url=ENRICHER_SERVICE_URL)
    app.run(host='0.0.0.0', port=8080, debug=False)
