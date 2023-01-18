from django.shortcuts import render
from django.http import HttpResponse

from PIL import Image
import os
import random
import string

import torch
import cv2
import matplotlib.pyplot as plt
import pandas as pd

def object_detection(image_path, df, image_name, detection_path):
        
    print(image_path)
    image = cv2.cvtColor(cv2.imread( image_path), cv2.COLOR_BGR2RGB)

    for i in df.index:
        xmin = df.iloc[i].xmin #* 2
        ymin = df.iloc[i].ymin #* 2
        xmax = df.iloc[i].xmax #* 2
        ymax = df.iloc[i].ymax #* 2
        label = df.iloc[i]['name']
        
        height = image.shape[0]
        width = image.shape[1]

        print('class:' , df.iloc[i]['name'])
        print('xmin:' , xmin)
        print('ymin:' , ymin)
        print('xmax:' , xmax)
        print('ymax:' , ymax)
        print('----------------------------')
            
        cv2.rectangle(image,
                      (int(xmin) , int(ymin) ),
                      (int(xmax) , int(ymax) ),
                      (0,255,0), thickness=2)

        ((label_width, label_height), _) = cv2.getTextSize(label, fontFace=cv2.FONT_HERSHEY_PLAIN, 
        fontScale=1.75, thickness=2)

        cv2.rectangle(
      image,
      (int(xmin) , int(ymin)),
      (int(xmin + label_width + label_width * 0.05), int(ymin + label_height + label_height * 0.25)),
      color=(255, 0, 0),
      thickness=cv2.FILLED
    )

        cv2.putText(
      image,
      label,
      org=(int(xmin), int(ymin + label_height + label_height * 0.25)), 
      fontFace=cv2.FONT_HERSHEY_PLAIN,
      fontScale=1.75,
      color=(255, 255, 255),
      thickness=2 )

    detected_image = detection_path + image_name
    cv2.imwrite(detected_image, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    return True

            


def random_characters(num):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))


def home(request):
    return render(request, 'complaints.html')


def upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        extention = '.' + image.name.split('.')[len(image.name.split('.')) - 1]

        uploads_path = 'static/images/uploads/'
        image_name = random_characters(9) + extention
        new_image = uploads_path + image_name
        save_image = Image.open(image)
        save_image = save_image.save(new_image)

        weight_path = 'yolov5/runs/train/exp/weights/best.pt'
        detection_path = 'static/images/detections/'
        model = torch.hub.load('yolov5', 'custom', path=weight_path, source='local')

        detection = model(new_image)
        detect = object_detection(new_image, detection.pandas().xyxy[0], image_name, detection_path)
        
        if detect == True:
            return render(request, 'complaints.html', context={'status': 'Image had been sent .. thanks!'})
        else:
            return render(request, 'complaints.html', context={'error': 'Error occurd'})


    else:
        return render(request, 'complaints.html', context={'error': 'Please select an image'})


