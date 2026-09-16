# core/emergency_system.py
import json
import random

class EmergencySystem:
    def __init__(self, template_file):
        with open(template_file, 'r') as f:
            self.templates = json.load(f)

    def simulate_emergency_call(self):
        return "Incoming call: Emergency! Please respond immediately."

    def simulate_emergency_sms(self, scenario):
        try:
            sms = random.choice(self.templates['emergency_sms'][scenario])
            return sms
        except KeyError:
            return "Invalid scenario."

# Example usage
if __name__ == "__main__":
    emergency = EmergencySystem('data/templates.json')
    print(emergency.simulate_emergency_call())
    print(emergency.simulate_emergency_sms('work'))
