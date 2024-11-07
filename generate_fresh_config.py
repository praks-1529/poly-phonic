import json
import itertools
from pathlib import Path

# File paths
vocoder_file = "vocoder.txt"
models_file = "model.txt"
output_json = "config.json"


def extract_last_two_parts(path):
    parts = Path(path).parts[-2:]
    return "_".join(parts)


def get_audio_src(model, vocoder):
    return 'https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_%s_%s_output.wav' % (
        extract_last_two_parts(model), extract_last_two_parts(vocoder))


# Read lines from both files and strip newlines
with open(vocoder_file, "r") as vf:
    vocoders = [line.strip() for line in vf.readlines()]

with open(models_file, "r") as mf:
    models = [line.strip() for line in mf.readlines()]

# Create every combination of vocoder and model with default values
data = [{"model": model, "vocoder": vocoder, "stars": 1, "link": get_audio_src(model, vocoder)}
        for model, vocoder in itertools.product(models, vocoders)]

# Write to JSON
with open(output_json, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Generated JSON saved to {output_json}")
