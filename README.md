# SDA2: Function as a Service

Workshop materials for the **SDA2 - Software Architecture** module at Berner Fachhochschule (BFH).

## Overview

This repository contains deployable microservices for learning Function as a Service (FaaS) concepts with CI/CD deployment:

- ✅ **Challenge 1:** Hello FaaS - First Function Deployment
- ✅ **Challenge 2:** Configuration Management
- ✅ **Challenge 3:** Structured Logging & Observability
- ✅ **Challenge 4:** Multi-Service Communication

## Repository Structure

Each challenge is in its own subfolder with a complete, deployable service:
```
challenge01-hello-faas/
├── README.md          # Challenge-specific instructions
├── app.py             # Service code
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container configuration
└── .env.example       # Environment variable template

challenge02-config/
challenge03-logging/
challenge04-service-a/
challenge04-service-b/
```

## Getting Started

### For Students

1. Fork this repository to your GitHub account
2. Navigate to a challenge subfolder (e.g., `challenge01-hello-faas/`)
3. Follow the instructions in that challenge's `README.md`
4. Deploy to Coolify using the provided instructions

### Deployment Workflow
```bash
# 1. Fork repo on GitHub
# 2. Clone to your machine
git clone https://github.com/YOUR-USERNAME/sda2-workshops.git
cd sda2-workshops/challenge01-hello-faas

# 3. Make changes
# 4. Push to trigger auto-deployment
git add .
git commit -m "Add goodbye endpoint"
git push
```

## Prerequisites

- GitHub account
- Access to Coolify instance (provided by instructor)
- Basic Python knowledge
- Basic Git knowledge

## License

MIT License - Copyright (c) 2025 Sebastian Höhn

## About

Developed for the Bachelor's program in Digital Business and AI at Berner Fachhochschule (BFH).