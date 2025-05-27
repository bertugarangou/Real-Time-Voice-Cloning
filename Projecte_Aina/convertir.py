import os
import csv
import subprocess
from pathlib import Path
import shutil

# Paths
tsv_path = "<ruta origen>\cv-corpus-21.0-2025-03-14\ca\validated.tsv"
clips_dir = "<ruta origen>\cv-corpus-21.0-2025-03-14\ca\clips"
output_dir = "<ruta destí>\Voice\Aina\"

os.makedirs(output_dir, exist_ok=True)

# Obre el fitxer empaquetat
with open(tsv_path, "r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter="\t")
    
    # Per cada fitxer de so
    for idx, row in enumerate(reader):
        #Extreu el so
        mp3_file = os.path.join(clips_dir, row["path"])
        if not os.path.exists(mp3_file):
            continue
        
        # Crea el fitxer
        base = f"utterance-{idx:04d}"
        wav_path = os.path.join(output_dir, f"{base}.wav")
        txt_path = os.path.join(output_dir, f"{base}.txt")
        text = row["sentence"].replace("|", "").strip()

        #codifica de mp3 a wav
        subprocess.run(["ffmpeg", "-y", "-i", mp3_file, "-ar", "22050", "-ac", "1", wav_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Escriu la transcripció
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

print("Conversió acabada.")
