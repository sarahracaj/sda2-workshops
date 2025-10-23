# SDA2 Challenge 1: Hello FaaS

## Overview
Deploy your first Function-as-a-Service using Coolify.

## Quick Start

### 1. Fork this repository
Click "Fork" button (top right on GitHub)

### 2. Clone to your machine
```bash
git clone https://github.com/bfh-teaching/sda2-workshops.git
cd sda2-workshops/sda2-challenge1-hello-faas
```

### 3. Test locally (optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:8080/hello

### 4. Deploy to Coolify

- Login to Coolify: https://coolify.ecys.ch
- Create a new Project
- Add a new Resource and choose Public Git Repo for that
- Paste your forked repo URL
- Add `challenge01-hello-faas` as your base path, because all challenges are in the same repo
- Set port: 8080
- Click "Deploy"

### 5. Your Task

Add a new endpoint `/goodbye` that returns:

```
{"message": "Goodbye, {name}!"}
```

Hint: Copy the /hello route and modify it.

### 6. Test your deployment

```bash
# Replace YOUR-SERVICE-URL with your Coolify URL
curl "https://YOUR-SERVICE-URL/goodbye?name=Student"
```

Expected output:
```
{"message": "Goodbye, Student!"}
```

## Troubleshooting

- **"Port already in use":** Stop other Python processes or change port 
- **"Module not found":** Run `pip install -r requirements.txt` 
- **"Deployment failed":** Check Coolify logs for error messages
