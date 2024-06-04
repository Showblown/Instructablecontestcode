import os
from openai import OpenAI
global important

client = OpenAI(
  api_key = ''
)

audio_file = open(r"output.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)
str(transcript)
output = r"output.wav"
important = transcript[:]
print(important)
