import os
from tabnanny import verbose
from pocketsphinx import LiveSpeech

global var
var = 1

bicara = LiveSpeech(lm=False, kws='belom buat', verbose=True, no_search=False, full_utt=False, buffer_size=1648, sampling_rate=16000)

if var == 1:
    os.system