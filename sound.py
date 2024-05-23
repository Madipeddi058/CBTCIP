import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Set parameters
duration = 15  # Recording duration in seconds
fs = 44100    # Sampling frequency (frames per second)

# Record audio
print("Recording audio...")
recorded_audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait for recording to complete

# Play back recorded audio
print("Playing back recorded audio...")
sd.play(recorded_audio, fs)
sd.wait()  # Wait for playback to finish

# Save recorded audio to a WAV file
output_filename = "recorded_audio.wav"
wav.write(output_filename, fs, recorded_audio)

print(f"Saved recorded audio to {output_filename}")