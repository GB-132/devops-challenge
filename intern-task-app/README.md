# Intern Task App: Kubernetes Deployment

This folder contains a containerized Python/Flask application and the Kubernetes manifests required to deploy it locally (e.g., via Docker Desktop / Kind).

## Prerequisites
- Docker Desktop (with Kubernetes enabled)
- `kubectl` CLI installed

## Project Structure
- `app.py`: Simple Python Flask application.
- `requirements.txt`: Python dependencies (Flask).
- `Dockerfile`: Instructions to containerize the application.
- `k8s/`: Contains Kubernetes deployment and service manifests.

## How to Build & Deploy

1. **Build the Docker Image:**
   ```bash
   docker build -t intern-app:latest .