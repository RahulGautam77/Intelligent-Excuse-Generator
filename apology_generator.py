# core/apology_generator.py
import json
import random

class ApologyGenerator:
    def __init__(self, template_file):
        with open(template_file, 'r') as f:
            self.templates = json.load(f)

    def generate_apology(self, tone):
        try:
            apology = random.choice(self.templates['apologies'][tone])
            return apology
        except KeyError:
            return "Invalid tone."

# Example usage
if __name__ == "__main__":
    generator = ApologyGenerator('data/templates.json')
    print(generator.generate_apology('formal'))
