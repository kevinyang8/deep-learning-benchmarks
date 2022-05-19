import requests
url="http://127.0.0.1:8080/predictions/maskrcnn"
file = open("persons.jpg", "rb")
bytes = file.read(-1)

from measure import measure
from measure import get_dph

def inference(image):
    return requests.post(url, data=image)

response = inference(bytes)
print(response.json())

loops = 100
measure(inference, [bytes], 'mask-rcnn', loops, get_dph())