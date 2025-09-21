import random
from locust import HttpUser, task, between
from pathlib import Path

try:
    QUERY_FILE_PATH = Path(__file__).parent.parent / 'data' / 'raw' / 'rq2' / 'rq2_queries.txt'
    with open(QUERY_FILE_PATH, 'r') as f:
        QUERIES = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    QUERIES = ["Explain the theory of relativity in simple terms."]

class LLMApiUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:5001"

    @task(3)
    def centralized_chatgpt(self):
        self._perform_query('/query/centralized', 'chatgpt')

    @task(2)
    def centralized_claude(self):
        self._perform_query('/query/centralized', 'claude')

    def _perform_query(self, endpoint, model_id):
        prompt = random.choice(QUERIES)
        self.client.post(endpoint, json={"prompt": prompt, "model_id": model_id}, name=f"{endpoint}_{model_id}")
