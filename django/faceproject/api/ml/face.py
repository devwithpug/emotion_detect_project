import torch
import torch.nn as nn
import torchvision
import torch.optim as optim
import torch.nn.functional as F
from torchvision import transforms, datasets, models
from torchvision.utils import make_grid
import os
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import cv2, requests
import base64

USE_CUDA = torch.cuda.is_available()
DEVICE = torch.device("cuda" if USE_CUDA else "cpu")
# DEVICE = torch.device("cpu")
print(DEVICE)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        self.conv4 = nn.Conv2d(64, 32, 3)
        self.fc1 = nn.Linear(2048, 1024)
        self.fc2 = nn.Linear(1024, 128)
        self.fc3 = nn.Linear(128, 7)
        self.batch_norm_16 = nn.BatchNorm2d(16)
        self.batch_norm_32 = nn.BatchNorm2d(32)
        self.batch_norm_64 = nn.BatchNorm2d(64)
        self.drop_out = nn.Dropout2d(p=0.3)

    def forward(self, x):
        x = F.relu(self.batch_norm_16(self.conv1(x)))
        x = F.relu(self.drop_out(F.max_pool2d(self.batch_norm_32(self.conv2(x)), 2)))
        x = F.relu(self.drop_out(F.max_pool2d(self.batch_norm_64(self.conv3(x)), 2)))
        x = F.relu(self.drop_out(self.batch_norm_32(self.conv4(x))))
        x = x.view(-1, 2048)

        x = F.relu(self.drop_out(self.fc1(x)))
        x = F.relu(self.drop_out(self.fc2(x)))
        x = self.fc3(x)

        return x


model = Model()

model.load_state_dict(torch.load('/Volumes/SSD/repo/emotion_detect_project/django/faceproject/templates/model.pt', map_location=DEVICE))
# model.load_state_dict(torch.load('/templates/model.pt', map_location=DEVICE))
model.eval()

facecasc = cv2.CascadeClassifier("/Volumes/SSD/repo/emotion_detect_project/django/faceproject/templates/haarcascade_frontalface_default.xml")
# facecasc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def do(encoded_string):
    print(encoded_string)
    encoded_string = encoded_string[0]

    nparr = np.asarray(bytearray(base64.b64decode(encoded_string)), dtype=np.uint8)
    nparr = cv2.resize(nparr, (48, 48), 0)

    nparr = nparr[np.newaxis, np.newaxis, :, :]

    nparr = torch.from_numpy(nparr).float()

    out = model(nparr)  # predict
    p = out.tolist()
    print(p)
    lis = out.flatten().tolist()
    lis = list(map(lambda x: x + 100, lis))
    result = [int(round(a / sum(lis), 3) * 100) for a in lis]
    classes = ['neutral', 'fearful', 'sad', 'happy', 'surprised', 'angry', 'disgusted']

    print("표정 :", classes)
    print("확률 :", result)

    maxindex = int(np.argmax(p))
    print("결과 :", classes[maxindex])

    return result


# url = input("input:")
#
# # spring 서버에서 base64 인코딩 문자열 전송
# raw = requests.get(url).content
# bb = base64.b64encode(raw)
# print(bb)