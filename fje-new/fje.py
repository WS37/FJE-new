import argparse
import json
import importlib
from context import Context

# 加载 JSON 文件
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def get_module(module_path):
    module_name, class_name = module_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

config = load_json("config.json")
parser = argparse.ArgumentParser(description="Funny JSON Explorer")
parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
parser.add_argument('-s', '--style', choices=list(config["style_strategies"].keys()), default='tree', help="Style to display JSON")
parser.add_argument('-i', '--icon_family', choices=list(config["icon_family_strategies"].keys()), default='card', help="Icon family to use")
args = parser.parse_args()

def main():
    data = load_json(args.file)
    example = Context(get_module(config["style_strategies"][args.style]), get_module(config["icon_family_strategies"][args.icon_family]))
    example.setStrategy()
    example.doSomething(data)

if __name__ == '__main__':
    main()
