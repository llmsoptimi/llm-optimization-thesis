import yaml
from pathlib import Path

def load_config():
    """Loads the API configuration file."""
    config_path = Path(__file__).parent.parent.parent / 'config' / 'config.yaml'
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return None
