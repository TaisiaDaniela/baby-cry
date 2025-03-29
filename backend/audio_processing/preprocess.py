#WaveGan - genereaza sunete bazandu-se pe input - generezi sunet sintetic
#metoda folosita  - generative adversarial networks(GANs)
#uniformizare in wav a sunetelor cu PYDUB

import os
import numpy as np
import soundfile as sf
import librosa
from pydub import AudioSegment

# Configurare foldere
input_main_folder = "C:\\Users\\taisi\\backend_frontend\\backend\\dataset\\donateacry_corpus - kaggle"
output_main_folder = "C:\\Users\\taisi\\backend_frontend\\backend\\dataset\\processed_dataset"

# Lungimea dorită în secunde
TARGET_DURATION = 3  # secunde
TARGET_SAMPLE_RATE = 16000  # Hz
TARGET_SAMPLES = TARGET_DURATION * TARGET_SAMPLE_RATE

# Creare folder de output dacă nu există
os.makedirs(output_main_folder, exist_ok=True)

# Procesare fiecare subfolder
categories = ["belly_pain_si_burping", "discomfort_lovire_cald_frig_nevoiedeiubire", "hungry", "tired"]
for category in categories:
    input_folder = os.path.join(input_main_folder, category)
    output_folder = os.path.join(output_main_folder, category)
    
    if not os.path.exists(input_folder):
        print(f"Folder inexistent: {input_folder}, îl sărim...")
        continue
    
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_base = os.path.join(output_folder, os.path.splitext(filename)[0])
        temp_wav_path = None
        
        # Convertire în WAV dacă este necesar
        if filename.lower().endswith(('.m4a', '.3gp')):
            audio = AudioSegment.from_file(input_path)
            temp_wav_path = output_base + "_converted.wav"
            audio.export(temp_wav_path, format="wav")
            input_path = temp_wav_path  # Suprascriem pentru a fi procesat corect
            
        if not input_path.lower().endswith(".wav"):
            continue
        
        # Citire fișier WAV
        audio, sample_rate = librosa.load(input_path, sr=TARGET_SAMPLE_RATE, mono=True)
        
        # Normalizare la int16
        audio = (audio * 32767).astype(np.int16)
        
        # Împărțire în segmente de 3 secunde
        total_samples = len(audio)
        num_chunks = total_samples // TARGET_SAMPLES
        remainder = total_samples % TARGET_SAMPLES
        
        for i in range(num_chunks):
            chunk = audio[i * TARGET_SAMPLES:(i + 1) * TARGET_SAMPLES]
            chunk_filename = f"{output_base}_part{i + 1}.wav"
            sf.write(chunk_filename, chunk, TARGET_SAMPLE_RATE)
            print(f"Saved: {chunk_filename}")
        
        # Dacă rămâne un segment mai scurt de 3 secunde, completăm cu sunet alb
        if remainder > 0:
            last_chunk = audio[-remainder:]
            padding = TARGET_SAMPLES - remainder
            white_noise = np.zeros(padding, dtype=np.int16)  # Folosim liniște, nu zgomot alb
            last_chunk = np.concatenate((last_chunk, white_noise))
            last_chunk_filename = f"{output_base}_part{num_chunks + 1}.wav"
            sf.write(last_chunk_filename, last_chunk, TARGET_SAMPLE_RATE)
            print(f"Saved: {last_chunk_filename}")
        
        # Șterge fișierul temporar dacă a fost creat
        if temp_wav_path and os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)

print("Procesare finalizată!")
