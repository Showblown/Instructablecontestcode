from pathlib import Path
from openai import OpenAI
from main import myoutput

client = OpenAI(
api_key = ''
)

speech_file_path = Path(__file__).parent / "final_output.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=myoutput
)

response.stream_to_file(r"final_output.mp3")
