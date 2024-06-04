import pydub
from pydub import AudioSegment
import pyaudio
from pydub.playback import play

song = AudioSegment.from_mp3('final_output.mp3')
pydub.playback.play(song)
