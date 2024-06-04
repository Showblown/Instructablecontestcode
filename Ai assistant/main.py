import os
import recorder
import speechtotext
import time
from openai import OpenAI
import subprocess

global generated_text
global myoutput
client = OpenAI(
    # This is the default and can be omitted
  api_key = ''
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a chatbot that spreads information"},
    {"role": "user", "content": "How do you say hello in spanish"}
  ]
)

myoutput = str(completion.choices[0].message)
myoutput = myoutput.removeprefix("ChatCompletionMessage(content=")
myoutput = myoutput.removesuffix(", role='assistant', function_call=None, tool_calls=None)")
print(myoutput)

import texttospeech
import audioplayer