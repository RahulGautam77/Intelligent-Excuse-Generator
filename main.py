import os
import datetime
import json
import uuid

from core.excuse_generator import ExcuseGenerator
from core.apology_generator import ApologyGenerator
from core.proof_generator import ProofGenerator
from core.emergency_system import EmergencySystem
from core.voice_generator import VoiceGenerator
from core.ranking_engine import RankingEngine
from core.scheduler import Scheduler


def save_text_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path


def main():
    print("=== Intelligent Excuse Generator ===")
    print("Please enter the following details:")

    # Input parameters
    scenario = input("Scenario (work, school, social, family) [work]: ").strip().lower() or 'work'
    urgency = input("Urgency (low, normal, high) [normal]: ").strip().lower() or 'normal'
    tone = input("Tone (formal, emotional) [formal]: ").strip().lower() or 'formal'

    # Prepare directories
    proofs_dir = os.path.join('proofs')
    os.makedirs(proofs_dir, exist_ok=True)

    # Initialize components with path to templates.json
    template_path = os.path.join('data', 'templates.json')
    excuse_gen = ExcuseGenerator(template_path)
    apology_gen = ApologyGenerator(template_path)
    proof_gen = ProofGenerator(template_path)
    emergency_sys = EmergencySystem(template_path)
    voice_gen = VoiceGenerator()
    ranking_eng = RankingEngine()
    scheduler = Scheduler()

    print("\nGenerating excuse...")
    excuse_text = excuse_gen.generate_excuse(scenario, urgency, tone)
    print(f"Excuse: {excuse_text}")

    print("\nGenerating apology...")
    apology_text = apology_gen.generate_apology(tone)
    print(f"Apology: {apology_text}")

    print("\nGenerating proofs...")
    chat_log = proof_gen.generate_fake_chat()
    location_log = proof_gen.generate_location_log()
    # Choose doctor's note for simplicity
    fake_doc = proof_gen.generate_fake_document('doctor_note')

    # Save proofs to text files with timestamp & uuid to ensure uniqueness
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]

    chat_filename = f"chat_log_{timestamp}_{unique_id}.txt"
    location_filename = f"location_log_{timestamp}_{unique_id}.txt"
    doc_filename = f"fake_doctor_note_{timestamp}_{unique_id}.txt"

    chat_path = save_text_file(proofs_dir, chat_filename, chat_log)
    location_path = save_text_file(proofs_dir, location_filename, location_log)
    doc_path = save_text_file(proofs_dir, doc_filename, fake_doc)

    print(f"Proofs saved:")
    print(f" - Fake chat log: {chat_path}")
    print(f" - Location log: {location_path}")
    print(f" - Fake document: {doc_path}")

    print("\nSimulating emergency call and SMS...")
    call_sim = emergency_sys.simulate_emergency_call()
    sms_sim = emergency_sys.simulate_emergency_sms(scenario)
    print(f"Emergency call simulation: {call_sim}")
    print(f"Emergency SMS simulation: {sms_sim}")

    print("\nGenerating voice output...")
    audio_filename = f"excuse_{timestamp}_{unique_id}.mp3"
    audio_path = os.path.join(proofs_dir, audio_filename)
    voice_gen.generate_voice(excuse_text, audio_path)
    print(f"Audio saved: {audio_path}")

    # Log usage for ranking and scheduling
    ranking_eng.log_excuse(excuse_text, outcome='neutral')  # in CLI no outcome data, using neutral
    scheduler.log_usage(datetime.datetime.now())
    ranked_score = ranking_eng.rank_excuses()
    next_usage_prediction = scheduler.predict_next_usage()

    print("\nRanking & Scheduling:")
    print(f" - Number of successful excuses logged: {ranked_score}")
    print(f" - Next likely excuse needed: {next_usage_prediction}")

    print("\n=== Excuse Generation Complete ===")


if __name__ == "__main__":
    main()

