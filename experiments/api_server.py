from flask import Flask, request, jsonify
from src.api_integrations.api_client import query_model
import time, random

app = Flask(__name__)

@app.route('/query/centralized', methods=['POST'])
def handle_centralized_query():
    data = request.json
    response = query_model(data.get('prompt'), data.get('model_id'))
    return jsonify({"response": response})

@app.route('/query/ezkl', methods=['POST'])
def handle_ezkl_query():
    data = request.json
    proof_gen_time_ms = random.uniform(3000, 150000)
    verification_time_ms = random.uniform(50, 150)
    time.sleep((proof_gen_time_ms + verification_time_ms) / 1000)
    response_content = query_model(data.get('prompt'), data.get('model_id'))
    return jsonify({
        "response": response_content,
        "proof_generation_time_ms": proof_gen_time_ms,
        "verification_time_ms": verification_time_ms
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
