import os
import time
import json
import psutil
from pathlib import Path
from src.api_integrations.api_client import query_model

def run_rq1():
    models = ['chatgpt', 'claude', 'deepseek']
    sessions = ['1.Multi-turn', '2.Cohesive', '3.Ethical'] 

    output_filename_map = {
        'chatgpt': 'allrunschatm.txt',
        'claude': 'allrunslaudem.txt',
        'deepseek': 'allrunsdeepm.txt'
    }

    base_data_path = Path(__file__).parent.parent / 'data' / 'raw' / 'rq1'

    for session_name in sessions:
        session_path = base_data_path / session_name
        session_path.mkdir(parents=True, exist_ok=True)

        query_file_map = {
            '1.Multi-turn': 'multi_queries.txt',
            '2.Cohesive': 'cohesive_queries.txt',
            '3.Ethical': 'ethical_queries.txt'
        }
        query_file = session_path / query_file_map.get(session_name)

        if not query_file.exists():
            print(f"Warning: Query file '{query_file}' not found. Skipping.")
            continue

        with open(query_file, 'r') as f:
            queries = [line.strip() for line in f if line.strip()]

        for model_id in models:
            results = []
            output_file = session_path / output_filename_map[model_id]

            for i, query in enumerate(queries):
                process = psutil.Process(os.getpid())
                start_time = time.perf_counter()
                response = query_model(query, model_id)
                end_time = time.perf_counter()

                results.append({
                    'query_index': i, 'query': query, 'response': response,
                    'latency_ms': (end_time - start_time) * 1000,
                    'cpu_percent': psutil.cpu_percent(),
                    'ram_mb': process.memory_info().rss / (1024 * 1024)
                })
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Results for {model_id} in {session_name} saved to {output_file}")

if __name__ == "__main__":
    run_rq1()
