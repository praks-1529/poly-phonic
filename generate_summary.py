# Description: This script reads the CPU and CUDA execution times from the log files and generates a
# markdown file with the combined execution times and sample audio links.
import pandas as pd
from pathlib import Path

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
    src = 'https://github.com/praks-1529/poly-phonic/blob/main/samples/speech_%s_%s_output.wav' % (
        extract_last_two_parts(model), extract_last_two_parts(vocoder))
    return f'<audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="{src}">Your browser does not support the audio tag.</audio>'


# Prepare the final DataFrame with the desired columns and formatting
final_df = pd.DataFrame({
    'Model': merged_df['Model'],
    'Vocoder': merged_df['Vocoder'],
    'Duration (device=cpu)': merged_df['Duration_cpu'],
    'Duration (device=cuda)': merged_df['Duration_cuda'],
    'SampeLink': merged_df.apply(lambda x: get_audio_path(x['Model'], x['Vocoder']), axis=1),
    # 'Sample':
})

# Convert the final DataFrame to a list of strings, with each line ending in '|'
with open('combined_execution_times.log', 'w') as f:
    # Write header with trailing '|'
    f.write('| ' + ' | '.join(final_df.columns) + ' |\n')
    # Write each row with trailing '|'
    for _, row in final_df.iterrows():
        f.write('| ' + ' | '.join(row.astype(str)) + ' |\n')

print("File 'combined_execution_times.log' created successfully!")
