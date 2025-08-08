# PenguinML Ops: Build, Test, Deploy

## Demo Video:
[![Watch the video](https://img.youtube.com/vi/PRLZrLmKjxE/maxresdefault.jpg)](https://youtu.be/PRLZrLmKjxE)

## Project Overview
This project is a machine learning API that predicts the species of a penguin based on features like bill length, bill depth, flipper length, body mass, year, sex, and island.
It uses FastAPI for the backend, runs inside Docker, and can be deployed to Google Cloud Run.

I tested the API locally and in the cloud under different traffic levels using Locust for load testing.

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


## My Answers and Final Analysis
What edge cases might break your model in production that aren't in your training data?
- If the model gets data outside the range it has seen before (like a penguin with extremely long flippers), it might give wrong answers. Missing values or strange categories (like "Unknown" for sex) could also cause problems.

What happens if your model file becomes corrupted?
- If the model file is broken, the API won’t be able to load it. Predictions would fail, and it would need to redeploy with a working model.

What's a realistic load for a penguin classification service?
- From what I can tell, since this is a relatively small model, a few hundred requests per second should be possible on cloud hosting, but this depends on memory, CPU, and scaling limits. For my Cloud Run settings I went with 2 gigs for reference.

How would you optimize if response times are too slow?
- From looking up how I can improve this online, it was suggested that I could use a faster model format like ONNX, run the API with more CPU/memory, or keep multiple instances running to avoid cold starts.

What metrics matter most for ML inference APIs?
- The most important metrics for ML inference APIs are response time, which measures how quickly results are returned, throughput which indicates the number of requests the system can handle per second, error rate which reflects the frequency of failures, and finanly resource usage including CPU and memory consumption.

Why is Docker layer caching important for build speed? (Did you leverage it?)
- Docker layer caching keeps unchanged layers from being rebuilt, making builds faster. Yes, I used it by putting dependencies before code in the Dockerfile.

What security risks exist with running containers as root?
- If someone hacks the container, they could have full control of the system. Running as a non-root user makes this much safer.

How does cloud auto-scaling affect your load test results?
- From my research, auto-scaling can lower response times when traffic grows by adding more instances. It can also cause cold starts when new instances spin up.

What would happen with 10x more traffic?
- If auto-scaling works well, the application should still respond fast. If not, we might see slower response times or failures.

How would you monitor performance in production?
- From what I did, I would use tools like Locust to periodically test request results and performance. But from my online reserach it seems like we can use tools like Google Cloud Monitoring or Prometheus to track response times, error rates, CPU/memory usage, and request counts.

How would you implement blue-green deployment?
- This kind of reminds me of A/B testing, but also different in that we would have two versions of the app blue and green. Then traffic goes to one version while we update the other. Once tested, we switch traffic to the new one without downtime. So we're not testing two different version of the app in the sense of experimentation to see which performs better, but this allows for the application to be live, while still being able to update it, without taking it down or potentially breaking it.

What would you do if deployment fails in production?
- I can roll back to the last working version quickly to keep the service running. This is why we store older docker images (GCP Artifact Repo) and use GitHub also to maintain version control.

What happens if your container uses too much memory?
- The container could crash or be stopped by the platform. I would need to increase memory limits or optimize the model to use less memory.
