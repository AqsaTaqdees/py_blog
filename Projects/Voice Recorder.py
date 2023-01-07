#Firstly install sounddevice module
pip install sounddevice


import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    #The first parameter is seconds, where you will enter the number of seconds you want to record your voice.
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")
    
#record.wav is the name of the recorded file; you can name it whatever you want
voice_recorder(10, "record.wav")
