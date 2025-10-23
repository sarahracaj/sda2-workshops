# SDA2 Challenge 2: Configuration Management

## Overview
Learn to externalize configuration using environment variables.

## The Problem
Hardcoding configuration in code is bad:
- ❌ Secrets exposed in Git
- ❌ Can't change config without redeploying code
- ❌ Different environments (dev/prod) require code changes

## The Solution: Environment Variables
- ✅ Secrets stay secret
- ✅ Change config in Coolify UI
- ✅ Same code runs in all environments

## Quick Start

### 1. Fork and clone this repository

```bash
git clone https://github.com/bfh-teaching/sda2-workshops.git
cd sda2-workshops/challenge02-config
```

### 2. Deploy to Coolify

1.	Create new service in Coolify
2.	Point to your forked repo
3.	Before deploying, add environment variables: 
    - API_KEY = your-secret-key-123
    - DEBUG = true
4.	Deploy

### 3. Your Task

Test the /config endpoint and verify it reads from environment variables.

```bash
curl https://YOUR-SERVICE-URL/config
Expected output:
{
  "api_key_set": true,
  "debug_mode": true
}
```

### 4. Bonus Challenge

Add a new endpoint /weather that:
- Requires WEATHER_API_KEY environment variable
- Returns error if not set
- Calls a weather API (or simulates it)

# Security Best Practices

## ✅ DO:
- Use environment variables for secrets
- Use .env.example to document required variables
 Add .env to .gitignore

## ❌ DON'T:
- Commit real API keys to Git
- Hardcode passwords in code
- Log sensitive values

# Troubleshooting

- "api_key_set: false": Environment variable not set in Coolify 
- "Cannot find module": Redeploy after adding requests to requirements.txt
