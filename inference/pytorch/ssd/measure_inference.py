import requests
import torch
from PIL import Image
import numpy
import torchvision.transforms as T
import io

# There are issues with formatting the input properly and sending it to the torchserve endpoint.

url="http://127.0.0.1:8080/predictions/my_tc"
# file = open("input.jpg", "rb")
# bytes = file.read(-1)
# print(bytes)

utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')
uri = 'http://images.cocodataset.org/val2017/000000397133.jpg'
input = utils.prepare_input(uri)
tensor = utils.prepare_tensor([input])

tensor = tensor.squeeze()
transform = T.ToPILImage()
img = transform(tensor)

buff = io.BytesIO()
torch.save(img, buff)
buff.seek(0)
bytes = buff.read()

from measure import measure
from measure import get_dph

def inference(image):
    return requests.post(url, data=image)

response = inference(bytes)
print(response)
#print(response.json())

loops = 100
measure(inference, [bytes], 'bert', loops, get_dph())