# Introduction
While using [CoquiTTS](https://github.com/coqui-ai/TTS) to train voice models on a custom dataset, I encountered numerous model and vocoder options, making it challenging to manually generate each combination to see how the generated vocals feel. This script automates the process of generating sample speech for all available English-language models and vocoders, simplifying the selection process and enabling easy comparisons of output quality across configurations.

With this script, you can regenerate samples using various model/vocoder options or simply listen to the pre-generated samples to get an initial sense of the output quality (from robotic to human-like). Enjoy exploring the possibilities!

# Installation
* Install [CoquiTTS](https://github.com/coqui-ai/TTS?tab=readme-ov-file#installation) first
* Some models require `speak-ng` to generate audio from provided text. So install that using standard instructuions

# Settings
All the runs were executed on a `g4dn.xlarge` EC2 machine which has 4 CPU and `NVIDIA T4` GPU. 

# Results
All the below speech samples are for below text

```
Rescuers found the crew scattered across the deck, frozen in terror, mouths open, eyes wide, and their bodies contorted as if witnessing something horrifying. There were no signs of injury or struggle, but something had clearly gone terribly wrong. Earlier, a haunting SOS message had been received, ending with the simple, I die. Right as they were about to tow the ship, a fire erupted from the cargo hold.  and they were forced to evacuate. They barely escaped before the ship exploded and sank, taking the evidence with it and leaving us with a dark unsolved mystery.
```

| Sample | Model | Vocoder | Duration (device=cpu) | Duration (device=cuda) | 
|-------|---------|-----------------------|------------------------|--------|
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/ljspeech/univnet | 27s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/ljspeech/hifigan_v2 | 25s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/ljspeech/multiband-melgan | 25s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/ek1/wavegrad | 1187s | 54s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/blizzard2013/hifigan_v2 | 26s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/vctk/hifigan_v2 | 23s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC | vocoder_models/en/sam/hifigan_v2 | 32s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/ljspeech/univnet | 16s | 16s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/ljspeech/hifigan_v2 | 13s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/ljspeech/multiband-melgan | 12s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/ek1/wavegrad | 1131s | 53s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/blizzard2013/hifigan_v2 | 14s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/vctk/hifigan_v2 | 13s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_glow-tts_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/glow-tts | vocoder_models/en/sam/hifigan_v2 | 20s | 17s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/ljspeech/univnet | 15s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/ljspeech/hifigan_v2 | 12s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/ljspeech/multiband-melgan | 10s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/ek1/wavegrad | 935s | 46s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/blizzard2013/hifigan_v2 | 12s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/vctk/hifigan_v2 | 11s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_speedy-speech_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/speedy-speech | vocoder_models/en/sam/hifigan_v2 | 18s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/ljspeech/univnet | 22s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/ljspeech/hifigan_v2 | 18s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/ljspeech/multiband-melgan | 17s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/ek1/wavegrad | 1072s | 52s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/blizzard2013/hifigan_v2 | 18s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/vctk/hifigan_v2 | 18s | 16s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DCA_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DCA | vocoder_models/en/sam/hifigan_v2 | 26s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/ljspeech/univnet | 18s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/ljspeech/hifigan_v2 | 16s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/ljspeech/multiband-melgan | 17s | 10s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/ek1/wavegrad | 17s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/blizzard2013/hifigan_v2 | 18s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/vctk/hifigan_v2 | 17s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits | vocoder_models/en/sam/hifigan_v2 | 17s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/ljspeech/univnet | 22s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/ljspeech/hifigan_v2 | 16s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/ljspeech/multiband-melgan | 15s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/ek1/wavegrad | 964s | 47s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/blizzard2013/hifigan_v2 | 16s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/vctk/hifigan_v2 | 17s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_fast_pitch_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/fast_pitch | vocoder_models/en/sam/hifigan_v2 | 23s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/ljspeech/univnet | 18s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/ljspeech/hifigan_v2 | 16s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/ljspeech/multiband-melgan | 17s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/ek1/wavegrad | 16s | 11s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/blizzard2013/hifigan_v2 | 16s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/vctk/hifigan_v2 | 17s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_vits--neon_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/vits--neon | vocoder_models/en/sam/hifigan_v2 | 16s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/ljspeech/univnet | 21s | 18s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/ljspeech/hifigan_v2 | 15s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/ljspeech/multiband-melgan | 15s | 19s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/ek1/wavegrad | 1049s | 54s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/blizzard2013/hifigan_v2 | 20s | 17s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/vctk/hifigan_v2 | 17s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_overflow_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/overflow | vocoder_models/en/sam/hifigan_v2 | 33s | 17s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/ljspeech/univnet | 23s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/ljspeech/hifigan_v2 | 18s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/ljspeech/multiband-melgan | 16s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/ek1/wavegrad | 1709s | 51s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/blizzard2013/hifigan_v2 | 21s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/vctk/hifigan_v2 | 18s | 16s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_neural_hmm_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/neural_hmm | vocoder_models/en/sam/hifigan_v2 | 33s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/ljspeech/univnet | 22s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/ljspeech/hifigan_v2 | 17s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/ljspeech/multiband-melgan | 17s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/ek1/wavegrad | 991s | 49s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/blizzard2013/hifigan_v2 | 17s | 20s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/vctk/hifigan_v2 | 17s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_ljspeech_tacotron2-DDC_ph_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/ljspeech/tacotron2-DDC_ph | vocoder_models/en/sam/hifigan_v2 | 24s | 19s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/ljspeech/univnet | 23s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/ljspeech/hifigan_v2 | 19s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/ljspeech/multiband-melgan | 20s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/ek1/wavegrad | 931s | 39s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/blizzard2013/hifigan_v2 | 23s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/vctk/hifigan_v2 | 20s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c50_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c50 | vocoder_models/en/sam/hifigan_v2 | 29s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/ljspeech/univnet | 25s | 15s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/ljspeech/hifigan_v2 | 18s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/ljspeech/multiband-melgan | 19s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/ek1/wavegrad | 893s | 42s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/blizzard2013/hifigan_v2 | 21s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/vctk/hifigan_v2 | 19s | 12s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_blizzard2013_capacitron-t2-c150_v2_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/blizzard2013/capacitron-t2-c150_v2 | vocoder_models/en/sam/hifigan_v2 | 27s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/ljspeech/univnet | 448s | 462s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/ljspeech/hifigan_v2 | 448s | 465s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/ljspeech/multiband-melgan | 463s | 470s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/ek1/wavegrad | 443s | 494s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/blizzard2013/hifigan_v2 | 510s | 452s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/vctk/hifigan_v2 | 451s | 438s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_multi-dataset_tortoise-v2_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/multi-dataset/tortoise-v2 | vocoder_models/en/sam/hifigan_v2 | 442s | 485s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_ljspeech_univnet_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/ljspeech/univnet | 62s | 16s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_ljspeech_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/ljspeech/hifigan_v2 | 56s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_ljspeech_multiband-melgan_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/ljspeech/multiband-melgan | 46s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_ek1_wavegrad_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/ek1/wavegrad | 47s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_blizzard2013_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/blizzard2013/hifigan_v2 | 45s | 14s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_vctk_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/vctk/hifigan_v2 | 47s | 13s |
| <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="https://github.com/praks-1529/poly-phonic/raw/refs/heads/main/samples/speech_jenny_jenny_sam_hifigan_v2_output.wav">Your browser does not support the audio tag.</audio> | tts_models/en/jenny/jenny | vocoder_models/en/sam/hifigan_v2 | 40s | 15s |