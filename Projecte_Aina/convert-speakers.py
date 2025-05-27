import os
import csv
import subprocess
from pathlib import Path
from collections import defaultdict

# Input paths
tsv_path = "C:/Users/albert.garangou/Desktop/Voice/Aina/cv-corpus-5.1-2020-06-22/ca/validated.tsv"
clips_dir = "C:/Users/albert.garangou/Desktop/Voice/Aina/cv-corpus-5.1-2020-06-22/ca/clips"
output_base = "C:/Users/albert.garangou/Desktop/Voice/Aina/LibriTTS/train-clean-100"

# Step 1: Detect accents in TSV
accents_set = set()
with open(tsv_path, "r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter="\t")
    for row in reader:
        accent = row["accent"].strip()
        if accent:
            accents_set.add(accent)

# Step 2: Ask user which accents to include
print("Available accents found in the dataset:")
for acc in sorted(accents_set):
    print(f" - {acc}")

selected = input("\nEnter comma-separated accents to include (e.g. central,balear): ").split(",")
selected_accents = set(a.strip() for a in selected)

print(f"\n✅ Including accents: {', '.join(selected_accents)}")

# Step 3: Process data
speaker_counts = defaultdict(int)

with open(tsv_path, "r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter="\t")
    for row in reader:
        accent = row["accent"].strip()
        if accent not in selected_accents:
            continue

        client_id = row["client_id"]
        text = row["sentence"].replace("|", "").strip()
        mp3_file = os.path.join(clips_dir, row["path"])
        if not os.path.exists(mp3_file):
            continue

        # Build output path: LibriTTS style
        speaker_dir = os.path.join(output_base, client_id, "book-001")
        os.makedirs(speaker_dir, exist_ok=True)

        utter_idx = speaker_counts[client_id]
        base = f"utterance-{utter_idx:04d}"
        wav_path = os.path.join(speaker_dir, f"{base}.wav")
        txt_path = os.path.join(speaker_dir, f"{base}.txt")

        # Convert audio
        subprocess.run(
            ["ffmpeg", "-y", "-i", mp3_file, "-ar", "22050", "-ac", "1", wav_path],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # Save transcript
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        speaker_counts[client_id] += 1

print("\n✅ Conversion complete with selected accents and speaker structure.")
