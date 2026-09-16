# core/proof_generator.py
import json
import random

class ProofGenerator:
    def __init__(self, template_file):
        with open(template_file, 'r') as f:
            self.templates = json.load(f)

    def generate_fake_chat(self):
        return "Fake chat log: [User ] Hey, I can't make it today due to an emergency."

    def generate_location_log(self):
        return "Location log: [User ] was last seen at [Location] at [Time]."

    def generate_fake_document(self, doc_type):
        try:
            document = random.choice(self.templates['fake_documents'][doc_type])
            return document
        except KeyError:
            return "Invalid document type."

# Example usage
if __name__ == "__main__":
    generator = ProofGenerator('data/templates.json')
    print(generator.generate_fake_chat())
    print(generator.generate_location_log())
    print(generator.generate_fake_document('doctor_note'))
