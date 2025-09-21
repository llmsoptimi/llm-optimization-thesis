import pandas as pd
import plotly.express as px
from pathlib import Path
import json

def generate_reports():
    processed_path = Path(__file__).parent.parent / 'data' / 'processed'
    raw_rq2_path = Path(__file__).parent.parent / 'data' / 'raw' / 'rq2'
    reports_path = Path(__file__).parent.parent / 'reports'
    reports_path.mkdir(exist_ok=True)

    try:
        rq1_df = pd.read_csv(processed_path / 'rq1_benchmark_results.csv')
        fig1 = px.line(rq1_df, x='session', y='latency_ms', color='model', title='RQ1: Latency vs. Accuracy')
        fig1.write_html(reports_path / 'rq1_latency_vs_accuracy.html')
        print("Generated RQ1 reports.")
    except FileNotFoundError:
        print("Could not find processed RQ1 data.")

    try:
        with open(raw_rq2_path / 'rq2_centralized_answers.txt', 'r') as f: cent_data = json.load(f)
        with open(raw_rq2_path / 'rq2_ezkl_answers.txt', 'r') as f: ezkl_data = json.load(f)

        rq2_df = pd.DataFrame(cent_data + ezkl_data)
        fig2 = px.line(rq2_df, x='load_level', y='throughput_rps', color='model', line_dash='setup', title='RQ2: Throughput vs. Users')
        fig2.write_html(reports_path / 'rq2_throughput_vs_users.html')
        print("Generated RQ2 reports.")
    except FileNotFoundError:
        print("Could not find RQ2 answer files.")

if __name__ == "__main__":
    generate_reports()
