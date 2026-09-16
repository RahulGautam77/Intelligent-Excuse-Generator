# core/excuse_generator.py
import json
import random

class ExcuseGenerator:
    def __init__(self, template_file):
        with open(template_file, 'r') as f:
            self.templates = json.load(f)

    def generate_excuse(self, scenario, urgency, tone):
        try:
            excuse = random.choice(self.templates['excuses'][scenario][urgency][tone])
            return excuse
        except KeyError:
            return "Invalid scenario, urgency, or tone."

# Example usage
if __name__ == "__main__":
    generator = ExcuseGenerator('data/templates.json')
    print(generator.generate_excuse('work', 'high', 'formal'))
