import os
import csv
import subprocess
from pathlib import Path
import shutil

tsv_path = "C:/Users/albert.garangou/Desktop/Voice/Aina/cv-corpus-5.1-2020-06-22/ca/validated.tsv"
clips_dir = "C:/Users/albert.garangou/Desktop/Voice/Aina/cv-corpus-5.1-2020-06-22/ca/clips"
output_dir = "C:/Users/albert.garangou/Desktop/Voice/Aina"

os.makedirs(output_dir, exist_ok=True)

# Conversion loop
with open(tsv_path, "r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter="\t")
    for idx, row in enumerate(reader):
        mp3_file = os.path.join(clips_dir, row["path"])
        if not os.path.exists(mp3_file):
            continue  # Skip missing files

        base = f"utterance-{idx:04d}"
        wav_path = os.path.join(output_dir, f"{base}.wav")
        txt_path = os.path.join(output_dir, f"{base}.txt")
        text = row["sentence"].replace("|", "").strip()

        # Convert mp3 to wav using ffmpeg
        subprocess.run(["ffmpeg", "-y", "-i", mp3_file, "-ar", "22050", "-ac", "1", wav_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Write transcript
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

print("â Conversion complete.")