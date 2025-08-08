from locust import HttpUser, task, between
import random

class LoadTestUser(HttpUser):
    wait_time = between(1, 5) 

    @task
    def predict_with_fixed_input(self):
        payload = {
            "bill_length_mm": 45.0,
            "bill_depth_mm": 15.0,
            "flipper_length_mm": 200,
            "body_mass_g": 4000,
            "year": 2008,
            "sex": "Male",
            "island": "Torgersen"
        }
        self.client.post("/predict", json=payload)
