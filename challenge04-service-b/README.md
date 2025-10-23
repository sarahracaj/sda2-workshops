# SDA2 Challenge 4: Service B (Data Enricher)

## Overview
This service receives data and adds enrichment metadata.

## Architecture
Service A → Service B (you are here)

## Quick Start

### 1. Deploy this service FIRST
```bash
git clone https://github.com/bfh-teaching/sda2-workshops.git
cd sda2-workshops/challenge04-service-b
```

Deploy to Coolify (no env vars needed)

### 2. Test independently

```bash
curl -X POST https://YOUR-SERVICE-B-URL/enrich \
  -H "Content-Type: application/json" \
  -d '{"name": "Test"}'
Expected output:
{
  "name": "Test",
  "enriched_at": "2025-10-22T10:30:00Z",
  "enriched": true
}
```

### 3. Copy your Service B URL

You'll need this for Service A's ENRICHER_SERVICE_URL environment variable.

# Your Task

1. Deploy and test this service
2. Use the URL in Service A configuration
3. Bonus: Add authentication (require API key header)
