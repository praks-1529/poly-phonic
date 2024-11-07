# Description: This script reads the CPU and CUDA execution times from the log files and generates a
# markdown file with the combined execution times and sample audio links.
import json
import pandas as pd
from pathlib import Path


class Config:
    def __init__(self, json_file):
        # Load the JSON data into a dictionary for easy access
        with open(json_file, "r") as f:
            self.data = json.load(f)

    def get_info(self, vocoder, model, info_type):
        """
        Fetches the requested info (either 'stars' or 'link') for the given vocoder and model.

        :param model: The model name as a string
        :param vocoder: The vocoder name as a string
        :param info_type: The type of information to fetch ('stars' or 'link')
        :return: The requested info if found, otherwise None
        """
        for entry in self.data:
            if entry["vocoder"] == vocoder and entry["model"] == model:
                return entry.get(info_type, None)
        return None


config = Config('config.json')
# Load CPU and CUDA log files into DataFrames
cpu_df = pd.read_csv('cpu.execution_times.log', sep='|', skipinitialspace=True, usecols=[
                     1, 2, 3], names=["Model", "Vocoder", "Duration"])
cuda_df = pd.read_csv('cuda.execution_times.log', sep='|', skipinitialspace=True, usecols=[
                      1, 2, 3], names=["Model", "Vocoder", "Duration"])

# Remove whitespace around column headers
cpu_df.columns = cpu_df.columns.str.strip()
cuda_df.columns = cuda_df.columns.str.strip()

# Remove whitespace around data entries
cpu_df = cpu_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
cuda_df = cuda_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Add a column to indicate the device
cpu_df['Device'] = 'cpu'
cuda_df['Device'] = 'cuda'

# Merge CPU and CUDA dataframes on Model and Vocoder
merged_df = pd.merge(cpu_df, cuda_df, on=[
                     "Model", "Vocoder"], suffixes=("_cpu", "_cuda"))

# Extract the last two parts of a path
# Example: /content/speech_combo/tacotron2/hifigan
# Output: tacotron2_hifigan


def extract_last_two_parts(path):
    parts = Path(path).parts[-2:]
    return "_".join(parts)


def get_audio_path(model, vocoder):
    src = 'https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_%s_%s_output.wav' % (
        extract_last_two_parts(model), extract_last_two_parts(vocoder))
    return f'[Play simple]({config.get_info(vocoder, model, "link")})'


def get_stars(model, vocoder):
    stars_to_str = {
        -1: '☆☆☆☆',
        0: '☆☆☆☆',
        1: '⭐☆☆☆',
        2: '⭐⭐☆☆',
        3: '⭐⭐⭐☆',
        4: '⭐⭐⭐⭐',
    }
    return stars_to_str[config.get_info(vocoder, model, "stars")]


# Prepare the final DataFrame with the desired columns and formatting
final_df = pd.DataFrame({
    'Sample': merged_df.apply(lambda x: get_audio_path(x['Model'], x['Vocoder']), axis=1),
    'Stars': merged_df.apply(lambda x: get_stars(x['Model'], x['Vocoder']), axis=1),
    'Model': merged_df['Model'],
    'Vocoder': merged_df['Vocoder'],
    'Duration (device=cpu)': merged_df['Duration_cpu'],
    'Duration (device=cuda)': merged_df['Duration_cuda'],
})

# Convert the final DataFrame to a list of strings, with each line ending in '|'
with open('combined_execution_times.log', 'w') as f:
    # Write header with trailing '|'
    f.write('| ' + ' | '.join(final_df.columns) + ' |\n')
    # Write each row with trailing '|'
    for _, row in final_df.iterrows():
        f.write('| ' + ' | '.join(row.astype(str)) + ' |\n')

print("File 'combined_execution_times.log' created successfully!")
