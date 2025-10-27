"""
SDA2 Challenge 3: Structured Logging
Demonstrates observability through structured JSON logging
"""

import logging
import json
import time
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # Just the message, we'll format as JSON
)
logger = logging.getLogger(__name__)

def log_event(event_type, **kwargs):
    """
    Log a structured event as JSON
    
    Args:
        event_type (str): Type of event (e.g., 'request_received', 'error')
        **kwargs: Additional fields to include in log
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_type,
        "service": "sda2-challenge3",
        **kwargs
    }
    logger.info(json.dumps(log_entry))

@app.route('/', methods=['GET'])
def home():
    log_event("home_page_accessed", method="GET")
    return jsonify({
        "service": "SDA2 Challenge 3",
        "status": "running",
        "endpoints": ["/process", "/slow", "/error"]
    })

@app.route('/process', methods=['POST'])
def process():
    """
    Process incoming data with comprehensive logging
    """
    start_time = time.time()
    
    # Log request received
    log_event("request_received", 
              endpoint="/process",
              method="POST")
    
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'data' not in data:
            log_event("request_error",
                     endpoint="/process",
                     error="Missing 'data' field",
                     duration_ms=int((time.time() - start_time) * 1000))
            return jsonify({"error": "Missing 'data' field"}), 400
        
        # Simulate processing
        log_event("processing_started",
                 endpoint="/process",
                 data_length=len(str(data['data'])))
        
        time.sleep(0.1)  # Simulate work
        
        result = {
            "status": "processed",
            "data": data['data'],
            "processed_at": datetime.utcnow().isoformat()
        }
        
        # Log success
        duration_ms = int((time.time() - start_time) * 1000)
        log_event("request_success",
                 endpoint="/process",
                 duration_ms=duration_ms,
                 status_code=200)
        
        return jsonify(result), 200
        
    except Exception as e:
        # Log error
        duration_ms = int((time.time() - start_time) * 1000)
        log_event("request_error",
                 endpoint="/process",
                 error=str(e),
                 error_type=type(e).__name__,
                 duration_ms=duration_ms)
        
        return jsonify({"error": str(e)}), 500

@app.route('/slow', methods=['GET'])
def slow_endpoint():
    """
    Intentionally slow endpoint to demonstrate performance logging
    """
    start_time = time.time()
    log_event("slow_request_started", endpoint="/slow")
    
    time.sleep(2)  # Simulate slow operation
    
    duration_ms = int((time.time() - start_time) * 1000)
    log_event("slow_request_completed",
             endpoint="/slow",
             duration_ms=duration_ms,
             warning="Endpoint took over 1 second")
    
    return jsonify({"message": "This was slow", "duration_ms": duration_ms})

@app.route('/error', methods=['GET'])
def error_endpoint():
    """
    Intentionally triggers an error for testing error logging
    """
    log_event("intentional_error_triggered", endpoint="/error")
    
    try:
        # This will raise a ZeroDivisionError
        result = 1 / 0
    except Exception as e:
        log_event("caught_exception",
                 endpoint="/error",
                 error=str(e),
                 error_type=type(e).__name__)
        return jsonify({"error": "Intentional error", "details": str(e)}), 500

# TODO: Add a new endpoint with comprehensive logging
# Track: request received, validation, processing steps, response
# Your code goes below this line

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()

    if not data or 'data' not in data:
        print("❌ Failed request: missing 'data' field")
        return jsonify({"error": "Missing 'data' field"}), 400

    print(f"✅ Received data: {data['data']}")
    return jsonify({
        "status": "success",
        "processed_data": data['data'].upper()
    })


if __name__ == '__main__':
    log_event("service_started", port=8080)
    app.run(host='0.0.0.0', port=8080, debug=False)
