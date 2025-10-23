# SDA2 Challenge 4: Service A (Data Processor)

## Overview
This service receives data, calls Service B to enrich it, and returns the result.

## Architecture
Client → Service A → Service B → Service A → Client

## Quick Start

### 1. Deploy Service B FIRST
See `sda2-challenge4-service-b` repository

### 2. Fork and clone this repo

```bash
git clone https://github.com/bfh-teaching/sda2-workshops.git
cd sda2-workshops/challenge04-service-a
```

### 3. Deploy to Coolify

Important: Set environment variable:
- ENRICHER_SERVICE_URL = https://your-service-b-url.com

### 4. Test the integration

```bash
curl -X POST https://YOUR-SERVICE-A-URL/aggregate \
  -H "Content-Type: application/json" \
  -d '{"name": "Student", "value": 42}'
Expected output:
{
  "name": "Student",
  "value": 42,
  "enriched_at": "2025-10-22T10:30:00Z",
  "enriched": true,
  "processed_by": "service-a"
}
```

## Your Task

1. Deploy both services
2. Test the communication
3. Add error handling: What happens if Service B is down?
4. Bonus: Add authentication between services (API key header)

# Troubleshooting

- "Connection refused": Check ENRICHER_SERVICE_URL is correct 
- "Timeout": Service B might be sleeping (Coolify auto-scales down) 
- "404 Not Found": Verify Service B endpoint is /enrich
