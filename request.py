import requests
import json
import cv2
from scipy.io.wavfile import read, write
import io


url = "http://35.192.179.200:5000/audio"
headers = {"content-type": "audio/wav"}


## This may look a bit intricate/useless, considering the fact that scipy's read() and write() function already return a
## numpy ndarray, but the BytesIO "hack" may be useful in case you get the wav not through a file, but trough some websocket or
## HTTP Post request. This should obviously work with any other sound format, as long as you have the proper decoding function

with open("audio1.wav", "rb") as wavfile:
    input_wav = wavfile.read()

# here, input_wav is a bytes object representing the wav object
rate, data = read(io.BytesIO(input_wav))

# data is a numpy ND array representing the audio data. Let's do some stuff with it
# reversed_data = data[::-1] #reversing it



# send HTTP request to the server
print("sending")
response = requests.post(url, data=rate, headers=headers)
print(response)
predictions = response.json()
print(predictions)
