# core/voice_generator.py
import pyttsx3

class VoiceGenerator:
    def __init__(self):
        self.engine = pyttsx3.init()

    def generate_voice(self, text, filename):
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()

# Example usage
if __name__ == "__main__":
    voice_gen = VoiceGenerator()
    voice_gen.generate_voice("I'm really sorry, but I can't make it today.", "excuse.mp3")
