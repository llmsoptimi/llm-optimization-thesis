import pandas as pd
import json
from pathlib import Path

def process_rq1():
    base_path = Path(__file__).parent.parent / 'data' / 'raw' / 'rq1'
    processed_path = Path(__file__).parent.parent / 'data' / 'processed'
    processed_path.mkdir(exist_ok=True)

    all_data = []
    model_map = {'allrunschatm.txt': 'ChatGPT-4 Turbo', 'allrunslaudem.txt': 'Claude 4 Sonnet', 'allrunsdeepm.txt': 'DeepSeek V3'}

    for session_folder in base_path.iterdir():
        if not session_folder.is_dir(): continue
        for model_file in session_folder.glob("*.txt"):
            if model_file.name not in model_map: continue
            with open(model_file, 'r') as f: data = json.load(f)
            df = pd.DataFrame(data)
            df['model'] = model_map[model_file.name]
            df['session'] = session_folder.name
            all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)
    output_file = processed_path / 'rq1_benchmark_results.csv'
    final_df.to_csv(output_file, index=False)
    print(f"Processed RQ1 data saved to {output_file}")

if __name__ == "__main__":
    process_rq1()
