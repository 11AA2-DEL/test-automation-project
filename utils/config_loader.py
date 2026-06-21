import os
import yaml
def load_config():
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),"config.yaml"
    )
    with open(config_path, "r", encoding = "utf-8") as f:
        data = yaml.safe_load(f)
        active = data["active_env"]
        return data[active]
CONFIG = load_config()