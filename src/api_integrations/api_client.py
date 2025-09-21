import requests
import json
from src.utils.config_loader import load_config

CONFIG = load_config()

def query_model(prompt, model_identifier, history=None):
    if not CONFIG:
        return {"error": "Configuration not loaded."}

    api_key = CONFIG['api_keys'].get(model_identifier)
    endpoint = CONFIG['api_endpoints'].get(model_identifier)
    model_name = CONFIG['model_names'].get(model_identifier)

    headers = {"Content-Type": "application/json"}

    if model_identifier in ['chatgpt', 'deepseek']:
        headers["Authorization"] = f"Bearer {api_key}"
        messages = history or []
        messages.append({"role": "user", "content": prompt})
        payload = {"model": model_name, "messages": messages, "max_tokens": 4096}
    elif model_identifier == 'claude':
        headers["x-api-key"] = api_key
        headers["anthropic-version"] = "2023-06-01"
        messages = history or []
        messages.append({"role": "user", "content": prompt})
        payload = {"model": model_name, "messages": messages, "max_tokens": 4096}
    else:
        return {"error": "Unknown model identifier."}

    try:
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload), timeout=180)
        response.raise_for_status()

        if model_identifier in ['chatgpt', 'deepseek']:
            return response.json()['choices'][0]['message']['content']
        elif model_identifier == 'claude':
            return response.json()['content'][0]['text']
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}
