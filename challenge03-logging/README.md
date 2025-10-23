# SDA2 Challenge 3: Structured Logging & Observability

## Overview
Add comprehensive logging to debug and monitor your service in production.

## Why Structured Logging?

### Traditional Logging (Bad)
User logged in Error occurred Request processed
**Problems:** 
- Can't search/filter
- No context
- Hard to aggregate

### Structured Logging (Good)
```json
{"timestamp": "2025-10-22T10:30:00", "event": "user_login", "user_id": "123"}
{"timestamp": "2025-10-22T10:30:05", "event": "error", "error": "DB timeout"}
{"timestamp": "2025-10-22T10:30:10", "event": "request_success", "duration_ms": 45}
```

### Benefits:

- ✅ Searchable by field
- ✅ Machine-readable
- ✅ Easy to aggregate/analyze

# Quick Start

## 1. Fork and clone 

```bash
git clone https://github.com/bfh-teaching/sda2-workshops.git
cd sda2-workshops/challenge03-logging
```

## 2. Deploy to Coolify
Standard deployment (no env vars needed for basic logging)

## 3. Your Task

Generate log entries by calling endpoints:

### Successful request

```bash
curl -X POST https://YOUR-URL/process \
  -H "Content-Type: application/json" \
  -d '{"data": "test"}'
```

### Failed request (missing data)

```bash
curl -X POST https://YOUR-URL/process \
  -H "Content-Type: application/json" \
  -d '{}'
```

## 4. View logs in Coolify

1. Go to your service in Coolify
2. Click "Logs" tab
3. Find your JSON log entries
4. Try searching for specific events: "event":"request_error"

## 5. Bonus Challenge

Add logging to a new endpoint that:
- Logs request received
- Logs processing steps
- Logs success/failure
- Logs response time

# Log Analysis Exercise

After generating logs, answer:
- How many requests succeeded vs. failed?
- What was the average response time?
- What errors occurred most frequently?

# Troubleshooting
- "Logs not appearing": Check Coolify log settings (might need refresh) 
- "JSON malformed": Ensure no syntax errors in log_event() function
