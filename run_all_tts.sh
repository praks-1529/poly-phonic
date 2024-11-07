#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <cpu|cuda>"
  exit 1
fi
device="$1"

# Read models and vocoders from files
models=$(<model.txt)
vocoders=$(<vocoder.txt)
ip_text = "Rescuers found the crew scattered across the deck, frozen in terror, mouths open, eyes wide, and their bodies contorted as if witnessing something horrifying. There were no signs of injury or struggle, but something had clearly gone terribly wrong. Earlier, a haunting SOS message had been received, ending with the simple, I die. Right as they were about to tow the ship, a fire erupted from the cargo hold.  and they were forced to evacuate. They barely escaped before the ship exploded and sank, taking the evidence with it and leaving us with a dark unsolved mystery."

run_tts() {
    #tts --device "$1" --text "<ENTER YOUR TEXT>" --model_name "$2" --vocoder_name "$3" --out_path $4
    tts --device "$1" --text "$ip_text" --model_name "$2" --vocoder_name "$3" --out_path $4
}

# Extract the last part of a path
# Example: /path/to/file.txt -> file.txt
extract_last_part() {
  local path="$1"
  echo "${path##*/}"
}

# Extract the last two parts of a path
# Example: /path/to/file.txt -> to_file.txt
extract_last_two_parts() {
  local path="$1"
  last_two="${path##*/}"
  second_last="${path%/*}"
  second_last="${second_last##*/}"
  echo "${second_last}_${last_two}"
}

# Log file for execution times
log_file="$device.execution_times.log"
echo "| Model | Vocoder | Duration |" > "$log_file"

# Loop through each model and vocoder combination
for model in $models; do
  for vocoder in $vocoders; do
    model_name=$(extract_last_two_parts "$model")
    vocoder_name=$(extract_last_two_parts "$vocoder")
    output_name="speech_${model_name}_${vocoder_name}_output.wav"
    
    # Record start time
    start_time=$(date +%s)
    
    echo "Running: run_tts $device $model $vocoder $output_name"
    #run_tts "$device" "$model" "$vocoder" "$output_name" || true
    
    # Record end time and calculate duration
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    
    # Log the duration for this combination
    echo "| $model | $vocoder | ${duration}s | " >> "$log_file"
  done
done