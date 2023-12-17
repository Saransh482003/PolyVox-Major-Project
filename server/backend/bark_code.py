# DO NOT IMPORT BARK YET, FIRST THEESE LINES:
# import os
# os.environ["XDG_CACHE_HOME"] = os.path.join("./bark_cache")
# NOW YOU CAN IMPORT BARK HERE
#multispeaker pre-trained model of bark
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import numpy as np
import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
# from workable_code import *


# download and load all models
preload_models()
def text_to_speech(speaker, Text, output_file, slowdown_factor=1):
    # Initialize an empty audio array
    combined_sounds = np.array([])

    # Calculate the number of segments
    l = int(len(Text) / 150) + (len(Text) % 150 > 0)
    for i in range(l): 
        # Extract the current segment
        segment = Text[i*150 : (i+1)*150]
        
        # Generate audio for the current segment
        audio_array = generate_audio(segment, history_prompt=speaker)
        audio_array = (audio_array * 32767).astype(np.int16)

        # Concatenate audio
        combined_sounds = np.concatenate((combined_sounds, audio_array))

    # save audio to disk with a lower sample rate
    write_wav(output_file, int(SAMPLE_RATE/slowdown_factor), combined_sounds.astype(np.int16))

