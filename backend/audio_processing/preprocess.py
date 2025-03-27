#WaveGan - genereaza sunete bazandu-se pe input - generezi sunet sintetic
#metoda folosita  - generative adversarial networks(GANs)
#uniformizare in wav a sunetelor cu PYDUB

import os
from pydub import AudioSegment

main_folder_path = "C:\\Users\\taisi\\backend_frontend\\backend\\dataset\\donateacry_corpus - kaggle"
output_main_folder = "C:\\Users\\taisi\\backend_frontend\\backend\\dataset\\processed_dataset" 

if not os.path.exists(output_main_folder):
    os.makedirs(output_main_folder)

for category_folder in os.listdir(main_folder_path):
    category_folder_path = os.path.join(main_folder_path, category_folder)
    
    if os.path.isdir(category_folder_path):
        print(f"Procesăm folderul: {category_folder}")
        
        output_category_folder = os.path.join(output_main_folder, category_folder)
        if not os.path.exists(output_category_folder):
            os.makedirs(output_category_folder)
        
        for file_name in os.listdir(category_folder_path):
            file_path = os.path.join(category_folder_path, file_name)
            
            if file_name.endswith(('.m4a', '.3gp', '.wav')):
                print(f"Procesăm fișierul: {file_name}")
                
                audio = AudioSegment.from_file(file_path)
                
                audio = audio.set_frame_rate(16000).set_channels(1)
                
                wav_file_path = os.path.join(output_category_folder, os.path.splitext(file_name)[0] + ".wav")
                
                audio.export(wav_file_path, format="wav")
                print(f"Fișierul salvat la: {wav_file_path}")
