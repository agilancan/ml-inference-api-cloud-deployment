# Penguin Species Prediction API

A production-ready **machine learning API** that predicts the species of a penguin based on morphological and environmental features.  
The API is built with **FastAPI**, containerized with **Docker**, and deployed to **Google Cloud Run** for scalability and reliability.  

It supports **RESTful predictions**, **automatic input validation**, and has been tested under various load scenarios using **Locust**.

---

## **Features**
- **ML-powered predictions** using a trained XGBoost model.
- **REST API** with interactive documentation (Swagger/OpenAPI).
- **Containerized deployment** for portability and scalability.
- **Cloud-native hosting** on Google Cloud Run with auto-scaling support.
- **Load testing and performance benchmarking** to validate production readiness.
- **Security best practices**, including non-root Docker containers and environment-based secret management.

---

## **Architecture**
1. **FastAPI Backend** – Serves predictions via `/predict` endpoint.
2. **XGBoost Model** – Trained on the Palmer Penguins dataset.
3. **Google Cloud Storage** – Hosts the serialized model artifact.
4. **Docker Container** – Optimized for performance and reproducibility.
5. **Google Cloud Run** – Deploys and auto-scales the application.
6. **Locust** – Evaluates API performance under real-world load conditions.

---

## **Tech Stack**
- **Python 3.10+**
- **FastAPI**
- **XGBoost**
- **Docker**
- **Google Cloud Run**
- **Locust (Load Testing)**

---

## **Setup & Usage**

### **1. Local Setup**

uv pip install -r requirements.txt
uv run uvicorn app.main:app --reload --port 8080


## Setup Instructions
1. Install Requirements
- I used uv for running Python commands and installing packages.
- uv pip install -r requirements.txt

2. Run Locally
- uv run uvicorn app.main:app --reload --port 8080
- http://localhost:8080
- Docs: http://localhost:8080/docs

3. Run in Docker
- docker build -t penguin-api .
- docker run -p 8080:8080 penguin-api

4. Run in Cloud Run
- https://penguin-backend-cloudran-151607684225.us-central1.run.app

5. Load Testing with Locust
- uv pip install locust
- uv run locust
- http://localhost:8089


## API Documentation
POST /predict
- Takes penguin data and returns the predicted species.
- Example request:
{
  "bill_length_mm": 45.1,
  "bill_depth_mm": 14.5,
  "flipper_length_mm": 210,
  "body_mass_g": 4500,
  "year": 2008,
  "sex": "Male",
  "island": "Torgersen"
}

- Example response:
{
  "species": "Adelie"
}


## Load Testing Results
Local Testing:
- Baseline (1 user, 60s): Response time 27.6 ms, 0 failures, 0.3 RPS
- Normal (10 users, 5 min): Response time 45.5 ms, 0 failures, 3.2 RPS

Cloud Testing:
- Baseline (1 user, 60s): Response time 85.1 ms, 0 failures, 0.3 RPS
- Normal (10 users, 5 min): Response time 83.7 ms, 0 failures, 3.2 RPS
- Stress (50 users, 2 min): Response time 76.2 ms, 0 failures, 16.1 RPS
- Spike (1 → 100 users, 1 min): Response time 75.3 ms, 0 failures, 28.2 RPS
